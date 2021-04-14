package io

import (
	"bufio"
	"encoding/csv"
	"fmt"
	"github.com/namhyun-gu/algorithm-script/internal/model"
	"os"
	"sort"
)

type Cache interface {
	Write(map[string]model.Solution) error
	Read() (map[string]model.Solution, error)
}

type CsvCache struct {
	Path string
}

func NewCsvCache(csvPath string) *CsvCache {
	return &CsvCache{Path: csvPath}
}

func (c CsvCache) Write(m map[string]model.Solution) error {
	file, err := os.OpenFile(c.Path, os.O_WRONLY|os.O_CREATE, 0)
	defer file.Close()

	if err != nil {
		return fmt.Errorf("can't open io (%v)", err.Error())
	}

	writer := bufio.NewWriter(file)
	csvWriter := csv.NewWriter(writer)

	solutions := make([]model.Solution, 0)
	for _, solution := range m {
		solutions = append(solutions, solution)
	}

	sort.Slice(solutions, func(i, j int) bool {
		return model.SolutionSorter(solutions[i], solutions[j])
	})

	for _, solution := range solutions {
		err := csvWriter.Write(solution.ToCsvRow())
		if err != nil {
			return err
		}
	}
	csvWriter.Flush()
	return nil
}

func (c CsvCache) Read() (map[string]model.Solution, error) {
	file, err := os.OpenFile(c.Path, os.O_RDONLY, 0)
	defer file.Close()

	if err != nil {
		return nil, fmt.Errorf("can't open io (%v)", err.Error())
	}

	reader := bufio.NewReader(file)
	csvReader := csv.NewReader(reader)

	rows, err := csvReader.ReadAll()
	if err != nil {
		return nil, err
	}

	data := make(map[string]model.Solution)
	for _, row := range rows {
		solution := model.NewSolution(row)
		data[solution.Id] = solution
	}
	return data, nil
}
