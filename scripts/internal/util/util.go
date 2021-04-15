package util

import (
	"fmt"
	"strings"
	"time"
)

func FormatTime(t time.Time) string {
	return fmt.Sprintf("%02d/%02d/%02d", t.Year(), t.Month(), t.Day())
}

func ConcatString(str ...string) string {
	return strings.Join(str, "")
}
