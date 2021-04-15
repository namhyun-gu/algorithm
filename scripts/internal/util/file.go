package util

import (
	"github.com/namhyun-gu/algorithm-script/internal/io"
	"os"
	"path/filepath"
	"strings"
)

func FilterFile(files []string, filter func(string) bool) []string {
	temp := make([]string, 0)
	for _, file := range files {
		if filter(file) {
			temp = append(temp, file)
		}
	}
	return temp
}

func MapFileInfo(paths []string) ([]io.File, error) {
	temp := make([]io.File, 0)
	for _, path := range paths {
		stat, err := os.Stat(path)
		if err != nil {
			return nil, err
		}

		name := stat.Name()
		name = strings.TrimSuffix(name, filepath.Ext(name))
		dirName := filepath.Base(filepath.Dir(path))

		temp = append(temp, io.File{
			Path:    path,
			DirName: dirName,
			Name:    name,
			Stat:    stat,
		})
	}
	return temp, nil
}
