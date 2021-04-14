package service

import (
	"fmt"
	"github.com/PuerkitoBio/goquery"
	"net/http"
)

func FetchSolution(solutionId string) (string, error) {
	url := fmt.Sprintf("https://www.acmicpc.net/problem/%s", solutionId)
	resp, err := http.Get(url)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()
	if resp.StatusCode != 200 {
		return "", fmt.Errorf("status code error: %d %s", resp.StatusCode, resp.Status)
	}

	doc, err := goquery.NewDocumentFromReader(resp.Body)
	if err != nil {
		return "", err
	}

	return doc.Find("#problem_title").Text(), nil
}
