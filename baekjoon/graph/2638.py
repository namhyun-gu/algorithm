from .. import util

example = """
8 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
"""
util.setinput(example)

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
paper = [[0 for _ in range(M)] for _ in range(N)]
cheese = 0

for n in range(N):
    line = list(map(int, input().split()))
    for m in range(M):
        if line[m] == 1:
            cheese += 1
        paper[n][m] = line[m]


def new_paper():
    return [[0 for _ in range(M)] for _ in range(N)]


def mark_blank_area():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.pop()
        for dx, dy in dirs:
            tx = x + dx
            ty = y + dy
            if 0 <= tx < M and 0 <= ty < N:
                if not visited[ty][tx] and paper[ty][tx] == 0:
                    blank[ty][tx] = 1
                    visited[ty][tx] = 1
                    queue.append((tx, ty))
                elif paper[ty][tx] == 1:
                    meet_cheese[ty][tx] += 1


def remove_cheese():
    removed = 0
    for n in range(N):
        for m in range(M):
            if meet_cheese[n][m] >= 2:
                paper[n][m] = 0
                blank[n][m] = 1
                removed += 1
    return removed


time = 0
while cheese > 0:
    blank = new_paper()
    meet_cheese = new_paper()
    mark_blank_area()
    cheese -= remove_cheese()
    time += 1

print(time)