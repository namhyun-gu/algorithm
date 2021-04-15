package main

import (
	"fmt"
	"github.com/namhyun-gu/algorithm-script/internal/io"
	"github.com/namhyun-gu/algorithm-script/internal/model"
	"github.com/namhyun-gu/algorithm-script/internal/service"
	"log"
	"os"
	"path/filepath"
)

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
	paths = io.FilterFile(paths, io.IsSolution)

	files, err := io.MapFileInfo(paths)
	if err != nil {
		log.Fatal(err)
	}
	newFiles := io.FilterNewer(files, data)

	if len(newFiles) == 0 {
		fmt.Println("Everything is up-to-date")
		return
	}

	fmt.Println("Updating new solution...")

	for _, file := range newFiles {
		solutionId := file.Name
		solutionType := file.DirName
		solutionPath := file.Path
		solutionDate := io.FormatTime(file.Stat.ModTime())

		solutionName, err := service.FetchSolution(solutionId)
		if err != nil {
			log.Fatal(err)
		}

		fmt.Printf("* %s: %s -> %s", solutionType, solutionId, solutionName)

		data[solutionId] = model.Solution{
			Id:   solutionId,
			Name: solutionName,
			Type: solutionType,
			Path: solutionPath,
			Date: solutionDate,
		}
	}

	fmt.Println("Updating README.md...")
	writer := io.NewReadmeWriter(filepath.Join(wd, "baekjoon/README.md"))
	err = writer.Write("baekjoon", data)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("README.md was updated successfully!")

	err = cache.Write(data)
	if err != nil {
		log.Fatal(err)
	}
}
