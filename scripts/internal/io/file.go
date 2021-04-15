package io

import (
	"os"
	"os/exec"
	"strings"
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
