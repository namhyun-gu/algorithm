package io

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type MarkdownWriter struct {
	Content []string
}

func NewMarkdownWriter() MarkdownWriter {
	return MarkdownWriter{
		Content: make([]string, 0),
	}
}

func (w *MarkdownWriter) Title(title string) *MarkdownWriter {
	w.append(concat("# ", title))
	w.NewLine()
	return w
}

func (w *MarkdownWriter) SubTitle(subTitle string) *MarkdownWriter {
	w.append(concat("## ", subTitle))
	w.NewLine()
	return w
}

func (w *MarkdownWriter) List(contents []string) *MarkdownWriter {
	for _, content := range contents {
		w.append(concat("- ", content))
		w.NewLine()
	}
	return w
}

func (w *MarkdownWriter) append(line string) {
	w.Content = append(w.Content, line)
}

func (w *MarkdownWriter) NewLine() *MarkdownWriter {
	w.append("\n")
	return w
}

func Link(text, url string) string {
	return fmt.Sprintf("[%s](%s)", text, url)
}

func (w *MarkdownWriter) Write(path string) error {
	err := os.Remove(path)
	if err != nil {
		return err
	}

	file, err := os.OpenFile(path, os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0)
	defer file.Close()
	if err != nil {
		return err
	}

	writer := bufio.NewWriter(file)
	_, err = writer.WriteString(strings.Join(w.Content, ""))
	if err != nil {
		return err
	}
	return writer.Flush()
}

func concat(str ...string) string {
	return strings.Join(str, "")
}
