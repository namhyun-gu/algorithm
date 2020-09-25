from .. import util

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
util.setinput(example)

import sys
input = sys.stdin.readline

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))


def is_same_color(x, y, n):
    color = paper[y][x]
    for i in range(n):
        for j in range(n):
            if color != paper[y + i][x + j]:
                return False
    return True


def divide(x, y, n):
    if n == 1:
        if paper[y][x] == 0:
            return (1, 0)
        else:
            return (0, 1)

    half = int(n / 2)
    areas = [(x, y), (x + half, y), (x, y + half), (x + half, y + half)]

    white = 0
    blue = 0
    for ax, ay in areas:
        if is_same_color(ax, ay, half):
            if paper[ay][ax] == 0:
                white += 1
            else:
                blue += 1
        else:
            area_white, area_blue = divide(ax, ay, half)
            white += area_white
            blue += area_blue
    return (white, blue)


white, blue = divide(0, 0, N)
print(white)
print(blue)
