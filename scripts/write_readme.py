from __future__ import annotations
from abc import ABCMeta, abstractmethod
from collections import defaultdict
import csv
from dataclasses import dataclass
import glob
from io import TextIOWrapper
from os import PathLike, path
from datetime import datetime
import os
from tqdm import tqdm
import time

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options


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

    def open_driver(self):
        options = Options()
        options.add_argument("--log-level=3")
        options.headless = True

        self.driver = webdriver.Chrome(
            executable_path="./scripts/chromedriver/chromedriver.exe",
            options=options,
            service_log_path=os.devnull,
        )

    def close_driver(self):
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
            title = " ".join(
                map(lambda it: it.capitalize(), type.replace("_", " ").split())
            )
            url = type.replace("_", "-")

            file.write(f"- [{title}](#{url})\n")
        file.write("\n")

    def write_type(self, file: TextIOWrapper, type: str, solutions: list[Solution]):
        title = " ".join(
            map(lambda it: it.capitalize(), type.replace("_", " ").split())
        )

        file.write(f"## {title}\n\n")
        for solution in solutions:
            file.write(f"- [{solution.name}]({solution.path})\n")
        file.write("\n")

    def group_solution(
        self, items: list[tuple[str, Solution]]
    ) -> dict[str, list[Solution]]:
        group = defaultdict(list)
        for item in items:
            _, solution = item
            group[solution.type].append(solution)
        return group


if __name__ == "__main__":
    cache = CsvCache("scripts/cache.csv")
    crawler = Crawler()
    writer = ReadmeWriter("README.md")

    files = FileUtils.get_files("baekjoon")
    solution_files = list(filter(FileUtils.is_solution, files))
    try:
        crawler.open_driver()
        pbar = tqdm(solution_files)
        for solution_file in pbar:
            file = File.from_path(solution_file)
            pbar.set_description(f"Process {file.dir_name}/{file.name}")
            if file.name not in cache:
                solution_name = crawler.fetch_name(file.name)
                cache.write(
                    int(file.name),
                    Solution(
                        solution_name, file.dir_name, file.path, file.modified_date
                    ),
                )
                for i in tqdm([0] * 5, desc="Wait", leave=False):
                    time.sleep(1)
    finally:
        crawler.close_driver()
        cache.flush()

        writer.write(title="algorithm-python", cache=cache)
