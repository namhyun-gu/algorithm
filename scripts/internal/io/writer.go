package io

import (
	"bufio"
	"fmt"
	"github.com/namhyun-gu/algorithm-script/internal/model"
	"os"
	"sort"
	"strings"
)

var typeOverride = map[string]string{
	"bfs": "BFS",
	"dfs": "DFS",
}

type ReadmeWriter struct {
	Path    string
	Content []string
}

func NewReadmeWriter(path string) ReadmeWriter {
	return ReadmeWriter{
		Path:    path,
		Content: make([]string, 0),
	}
}

func (w ReadmeWriter) Write(title string, data map[string]model.Solution) error {
	err := os.Remove(w.Path)
	if err != nil {
		return err
	}

	file, err := os.OpenFile(w.Path, os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0)
	defer file.Close()

	if err != nil {
		return err
	}

	writer := bufio.NewWriter(file)
	types, solutions := w.groupSolution(data)

	w.writeTitle(title)
	w.writeTOC(types)
	for _, t := range types {
		w.writeSolutions(t, solutions[t])
	}

	_, err = writer.WriteString(strings.Join(w.Content, ""))
	if err != nil {
		return err
	}
	return writer.Flush()
}

func (w *ReadmeWriter) Append(line string) {
	w.Content = append(w.Content, line)
}

func (w *ReadmeWriter) writeTitle(title string) {
	w.Append(fmt.Sprintf("# %s\n\n", title))
}

func (w *ReadmeWriter) writeTOC(types []string) {
	for _, t := range types {
		title := typeToTitle(t)
		url := strings.ReplaceAll(t, "_", "-")

		w.Append(fmt.Sprintf("- [%s](#%s)\n", title, url))
	}
	w.Append("\n")
}

func (w *ReadmeWriter) writeSolutions(t string, solutions []model.Solution) {
	title := typeToTitle(t)
	w.Append(fmt.Sprintf("## %s\n\n", title))

	for _, solution := range solutions {
		solutionUrl := strings.ReplaceAll(solution.Path, "\\", "/")
		content := fmt.Sprintf("- [%s (%s)](../%s)\n", solution.Name, solution.Id, solutionUrl)
		w.Append(content)
	}
	w.Append("\n")
}

func (w ReadmeWriter) groupSolution(data map[string]model.Solution) ([]string, map[string][]model.Solution) {
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
