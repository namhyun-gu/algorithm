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

	fileInfos, err := io.MapFileInfo(paths)
	if err != nil {
		log.Fatal(err)
	}
	fileInfos = io.FilterNewer(fileInfos, data)

	if len(fileInfos) > 0 {
		fmt.Printf("Updating new solution...(%d)\n", len(fileInfos))

		for _, file := range fileInfos {
			solutionName, err := service.FetchSolution(file.Name)
			if err != nil {
				log.Fatal(err)
			}
			data[file.Name] = model.Solution{
				Id:   file.Name,
				Name: solutionName,
				Type: file.DirName,
				Path: file.Path,
				Date: io.FormatTime(file.Stat.ModTime()),
			}
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
