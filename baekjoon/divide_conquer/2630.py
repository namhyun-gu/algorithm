import io
import sys

example = """
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def is_same_color(paper, x, y, n):
    temp = paper[x][y]
    for _x in range(x, x + n):
        for _y in range(y, y + n):
            if paper[_x][_y] != temp:
                return False
    return True


def make_paper(paper, x, y, n):
    white = 0
    blue = 0

    if n == 1:
        if paper[x][y] == "0":
            white += 1
        else:
            blue += 1
    else:
        if is_same_color(paper, x, y, n):
            if paper[x][y] == "0":
                white = 1
            else:
                blue = 1
        else:
            half = n // 2

            for _x in [x, x + half]:
                for _y in [y, y + half]:
                    _w, _b = make_paper(paper, _x, _y, half)
                    white += _w
                    blue += _b
    return white, blue


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    paper = [input().strip().split() for _ in range(N)]

    white, blue = make_paper(paper, 0, 0, N)

    print(white)
    print(blue)