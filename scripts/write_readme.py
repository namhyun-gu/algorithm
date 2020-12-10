from __future__ import annotations

import csv
import glob
import os
import time
from abc import ABCMeta, abstractmethod
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from io import TextIOWrapper
from os import PathLike, path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from tqdm import tqdm


@dataclass
class File:
    path: str
    name: str
    dir_name: str
    modified_date: str

    @staticmethod
    def from_path(filepath: PathLike) -> File:
        name = path.splitext(path.basename(filepath))[0]
        dir_name = path.basename(path.normpath(path.dirname(filepath)))
        modified_time = path.getmtime(filepath)
        modified_date = datetime.fromtimestamp(modified_time).strftime("%Y/%m/%d")

        return File(filepath, name, dir_name, modified_date)


@dataclass
class Solution:
    name: str
    type: str
    path: str
    date: str


class CacheInterface(metaclass=ABCMeta):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, id: int, solution: Solution):
        pass

    @abstractmethod
    def flush(self):
        pass

    @abstractmethod
    def get_items(self) -> list[tuple[str, Solution]]:
        pass

    @abstractmethod
    def __contains__(self, name: str) -> bool:
        pass

    @abstractmethod
    def __getitem__(self, name: str) -> Solution:
        pass


class CsvCache(CacheInterface):
    def __init__(self, csv_path: str) -> None:
        self.__temp: dict[str, Solution] = {}
        self.__csv_path = csv_path
        self.read()

    def read(self):
        with open(self.__csv_path, encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                id, name, type, path, date = row
                self.__temp[id] = Solution(name, type, path, date)

    def write(self, id: int, solution: Solution):
        self.__temp[id] = solution

    def flush(self):
        with open(self.__csv_path, "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for item in self.get_items():
                id, solution = item
                writer.writerow(
                    [id, solution.name, solution.type, solution.path, solution.date]
                )

    def get_items(self) -> list[tuple[str, Solution]]:
        return sorted(
            self.__temp.items(), key=lambda it: (it[1].type, it[1].date, it[1].name)
        )

    def __contains__(self, name: str) -> bool:
        return name in self.__temp

    def __getitem__(self, name: str) -> Solution:
        return self.__temp[name]


class FileUtils:
    @staticmethod
    def get_files(root_path: str) -> list[str]:
        return glob.glob(f"{root_path}/*/*.py")

    @staticmethod
    def is_solution(file_path: str) -> bool:
        name = path.basename(file_path)
        return name not in ["__init__.py"]


class Crawler:
    def __init__(self) -> None:
        self.driver = None

    def is_opened(self):
        return self.driver != None

    def open_driver(self):
        if not self.is_opened():
            options = Options()
            options.add_argument("--log-level=3")
            options.headless = True

            self.driver = webdriver.Chrome(
                executable_path="./scripts/chromedriver/chromedriver.exe",
                options=options,
                service_log_path=os.devnull,
            )

    def close_driver(self):
        if self.is_opened():
            self.driver.close()

    def fetch_name(self, problem_id: int) -> str:
        self.driver.get(f"https://www.acmicpc.net/problem/{problem_id}")
        elem: WebElement = self.driver.find_element_by_id("problem_title")
        title = elem.text
        return title


class Logger:
    @staticmethod
    def d(tag: str, message: str):
        print(f"[DEBUG]\t{tag}\t{message}")

    @staticmethod
    def i(tag: str, message: str):
        print(f"[INFO] \t{tag}\t{message}")


class ReadmeWriter:
    def __init__(self, readme_path: str) -> None:
        self.__readme_path = readme_path

    def write(self, title: str, cache: CacheInterface):
        group_solutions = self.group_solution(cache.get_items())
        types = sorted(group_solutions.keys())
        with open(self.__readme_path, "w", encoding="utf-8") as readme:
            readme.write(f"# {title}\n\n")
            self.write_toc(readme, types)

            for type in types:
                solutions = sorted(
                    group_solutions[type], key=lambda it: (it.date, it.name)
                )
                self.write_type(readme, type, solutions)

    def write_toc(self, file: TextIOWrapper, types: list[str]):
        for type in types:
            title = self.to_title(type)
            url = type.replace("_", "-")

            file.write(f"- [{title}](#{url})\n")
        file.write("\n")

    def write_type(self, file: TextIOWrapper, type: str, solutions: list[Solution]):
        title = self.to_title(type)
        file.write(f"## {title}\n\n")
        for solution in solutions:
            solution_url = solution.path.replace("\\", "/")
            file.write(f"- [{solution.name}]({solution_url})\n")
        file.write("\n")

    def group_solution(
        self, items: list[tuple[str, Solution]]
    ) -> dict[str, list[Solution]]:
        group = defaultdict(list)
        for item in items:
            _, solution = item
            group[solution.type].append(solution)
        return group

    def to_title(self, type: str) -> str:
        type_override = {"bfs": "BFS", "dfs": "DFS"}

        if type in type_override:
            return type_override[type]
        else:
            title = type.replace("_", " ").split()
            title = map(lambda it: it.capitalize(), title)
            return " ".join(title)


def is_newer(cache: CacheInterface, file: File) -> bool:
    if file.name not in cache:
        return True
    else:
        exists = cache[file.name]
        if file.dir_name != exists.type:
            return True
        if file.path != exists.path:
            return True
        return False


if __name__ == "__main__":
    print("Updating README.md...")

    cache = CsvCache("scripts/cache.csv")
    crawler = Crawler()
    writer = ReadmeWriter("README.md")

    files = FileUtils.get_files("baekjoon")
    files = filter(FileUtils.is_solution, files)
    files = map(File.from_path, files)
    files = filter(lambda file: is_newer(cache, file), files)
    files = list(files)

    if files:
        try:
            crawler.open_driver()

            pbar = tqdm(files, leave=False)
            for idx, file in enumerate(pbar):
                pbar.set_description(f"Process {file.dir_name}/{file.name}")
                id = file.name
                name = crawler.fetch_name(id)
                solution = Solution(
                    name=name, type=file.dir_name, path=file.path, date=file.modified_date
                )
                cache.write(id, solution)

                if idx < len(files) - 1:
                    for _ in tqdm([0] * 5, desc="Wait", leave=False):
                        time.sleep(1)
        finally:
            crawler.close_driver()
            cache.flush()
            writer.write(title="algorithm-python", cache=cache)
    print("README.md was updated successfully!")