package model

type Solution struct {
	Id   string
	Name string
	Type string
	Path string
	Date string
}

func NewSolution(csvRow []string) Solution {
	solutionId := csvRow[0]
	solutionName := csvRow[1]
	solutionType := csvRow[2]
	solutionPath := csvRow[3]
	solutionDate := csvRow[4]

	return Solution{
		Id:   solutionId,
		Name: solutionName,
		Type: solutionType,
		Path: solutionPath,
		Date: solutionDate,
	}
}

func (s Solution) ToCsvRow() []string {
	row := make([]string, 0)
	row = append(row, s.Id)
	row = append(row, s.Name)
	row = append(row, s.Type)
	row = append(row, s.Path)
	row = append(row, s.Date)
	return row
}

func SolutionSorter(a, b Solution) bool {
	if a.Type < b.Type {
		return true
	}
	if a.Type > b.Type {
		return false
	}

	if a.Date < b.Date {
		return true
	}
	if a.Date > b.Date {
		return false
	}
	return a.Name < b.Name
}
