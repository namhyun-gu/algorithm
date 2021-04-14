package io

import (
	"fmt"
	"github.com/namhyun-gu/algorithm-script/internal/model"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"time"
)

type File struct {
	Path    string
	DirName string
	Name    string
	Stat    os.FileInfo
}

func FetchFiles(path string) ([]string, error) {
	cmd := exec.Command("git", "diff", "--name-only", "HEAD", path)
	output, err := cmd.Output()
	if err != nil {
		return nil, err
	}
	s := string(output)
	if len(s) == 0 {
		return []string{}, nil
	}
	return strings.Split(strings.TrimSpace(s), "\n"), nil
}

func FilterFile(files []string, filter func(string) bool) []string {
	temp := make([]string, 0)
	for _, file := range files {
		if filter(file) {
			temp = append(temp, file)
		}
	}
	return temp
}

func MapFileInfo(paths []string) ([]File, error) {
	temp := make([]File, 0)
	for _, path := range paths {
		stat, err := os.Stat(path)
		if err != nil {
			return nil, err
		}

		name := stat.Name()
		name = strings.TrimSuffix(name, filepath.Ext(name))
		dirName := filepath.Base(filepath.Dir(path))

		temp = append(temp, File{
			Path:    path,
			DirName: dirName,
			Name:    name,
			Stat:    stat,
		})
	}
	return temp, nil
}

func IsSolution(file string) bool {
	excluded := map[string]struct{}{
		"__init__.py":  {},
		"README.md":    {},
		"profile.psm1": {},
	}
	base := filepath.Base(file)
	_, exists := excluded[base]
	return !exists
}

func FormatTime(t time.Time) string {
	return fmt.Sprintf("%02d/%02d/%02d", t.Year(), t.Month(), t.Day())
}

func FilterNewer(files []File, cache map[string]model.Solution) []File {
	temp := make([]File, 0)
	for _, file := range files {
		if IsNewer(file, cache) {
			temp = append(temp, file)
		}
	}
	return temp
}

func IsNewer(file File, cacheData map[string]model.Solution) bool {
	cache, exist := cacheData[file.Name]
	if !exist {
		return true
	}

	if file.DirName != cache.Type {
		return true
	}
	if file.Path != cache.Path {
		return true
	}
	return false
}
