package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"sort"
	"strings"

	"github.com/namhyun-gu/algorithm-script/internal/io"
	"github.com/namhyun-gu/algorithm-script/internal/model"
	"github.com/namhyun-gu/algorithm-script/internal/service"
	"github.com/namhyun-gu/algorithm-script/internal/util"
)

var typeOverride = map[string]string{
	"bfs": "BFS",
	"dfs": "DFS",
}

func main() {
	wd, err := os.Getwd()
	if err != nil {
		log.Fatal(err)
	}

	var cache io.Cache
	cache = io.NewCsvCache(filepath.Join(wd, "scripts/cache.csv"))

	data, err := cache.Read()
	if err != nil {
		log.Fatal(err)
	}

	paths, err := io.FetchFiles("baekjoon")
	paths = util.FilterFile(paths, util.IsSolution)

	files, err := util.MapFileInfo(paths)
	if err != nil {
		log.Fatal(err)
	}
	newFiles := util.FilterNewer(files, data)

	if len(newFiles) == 0 {
		fmt.Println("Everything is up-to-date")
		return
	}

	fmt.Println("Updating new solution...")

	for _, file := range newFiles {
		solutionId := file.Name
		solutionType := file.DirName
		solutionPath := file.Path
		solutionDate := util.FormatTime(file.Stat.ModTime())

		solutionName, err := service.FetchSolution(solutionId)
		if err != nil {
			log.Fatal(err)
		}

		fmt.Printf("* %s: %s -> %s\n", solutionType, solutionId, solutionName)

		data[solutionId] = model.Solution{
			Id:   solutionId,
			Name: solutionName,
			Type: solutionType,
			Path: solutionPath,
			Date: solutionDate,
		}
	}

	fmt.Println("Updating README.md...")
	err = WriteReadme(filepath.Join(wd, "baekjoon/README.md"), data)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("README.md was updated successfully!")

	err = cache.Write(data)
	if err != nil {
		log.Fatal(err)
	}
}

func WriteReadme(path string, data map[string]model.Solution) error {
	concat := util.ConcatString
	link := io.Link

	types, solutions := groupSolution(data)

	writer := io.NewMarkdownWriter()
	writer.Title("baekjoon").NewLine()

	typeList := make([]string, 0)
	for _, t := range types {
		text := typeToTitle(t)
		url := strings.ReplaceAll(t, "_", "-")

		typeItem := link(text, concat("#", url))
		typeList = append(typeList, typeItem)
	}
	writer.List(typeList).NewLine()

	for _, t := range types {
		writer.SubTitle(typeToTitle(t)).NewLine()

		solutionList := make([]string, 0)
		for _, solution := range solutions[t] {
			text := concat(solution.Name, " (", solution.Id, ")")
			url := strings.ReplaceAll(solution.Path, "\\", "/")

			solutionItem := link(text, concat("../", url))
			solutionList = append(solutionList, solutionItem)
		}
		writer.List(solutionList).NewLine()
	}
	return writer.Write(path)
}

func groupSolution(data map[string]model.Solution) ([]string, map[string][]model.Solution) {
	types := make([]string, 0)
	m := make(map[string][]model.Solution)
	for _, solution := range data {
		if val, exist := m[solution.Type]; exist {
			val = append(val, solution)
			m[solution.Type] = val
		} else {
			types = append(types, solution.Type)

			s := make([]model.Solution, 0)
			s = append(s, solution)
			m[solution.Type] = s
		}
	}

	sort.Strings(types)

	for _, solutions := range m {
		sort.Slice(solutions, func(i, j int) bool {
			return model.SolutionSorter(solutions[i], solutions[j])
		})
	}
	return types, m
}

func typeToTitle(t string) string {
	var title string
	if val, exist := typeOverride[t]; exist {
		title = val
	} else {
		title = strings.Title(strings.ReplaceAll(t, "_", " "))
	}
	return title
}
