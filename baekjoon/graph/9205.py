from .. import util

example = """
2
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000
"""
util.setinput(example)

# Ref: https://tinyurl.com/y5vjlxsx
import sys
from collections import deque
input = sys.stdin.readline


def manhattan_dist(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1 - x2) + abs(y1 - y2)


def bfs(graph, start, end):
    visited = [0] * len(graph)
    visited[0] = 1
    queue = deque([start])

    be_happy = False
    while queue:
        current = queue.popleft()
        if current == end:
            be_happy = True

        for idx in range(len(graph)):
            if not visited[idx] and graph[current][idx] == 1:
                visited[idx] = 1
                queue.append(idx)

    return be_happy


T = int(input())
for _ in range(T):
    n = int(input())
    graph = [[-1 for _ in range(n + 2)] for _ in range(n + 2)]
    coords = []
    for idx in range(n + 2):
        x, y = map(int, input().split())
        coords.append((x, y))

    for i in range(n + 2):
        for j in range(n + 2):
            dist = manhattan_dist(coords[i], coords[j])
            if dist != 0 and dist <= 1000:
                graph[i][j] = 1

    be_happy = bfs(graph, 0, n + 1)
    if be_happy:
        print("happy")
    else:
        print("sad")
