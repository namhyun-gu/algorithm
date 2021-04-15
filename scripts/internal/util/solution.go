package util

import (
	"github.com/namhyun-gu/algorithm-script/internal/io"
	"github.com/namhyun-gu/algorithm-script/internal/model"
	"path/filepath"
)

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

func FilterNewer(files []io.File, cache map[string]model.Solution) []io.File {
	temp := make([]io.File, 0)
	for _, file := range files {
		if IsNewer(file, cache) {
			temp = append(temp, file)
		}
	}
	return temp
}

func IsNewer(file io.File, cacheData map[string]model.Solution) bool {
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
