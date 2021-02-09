import io
import sys

example = """
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
"""
sys.stdin = io.StringIO(example.strip())

import sys
from collections import deque

input = sys.stdin.readline

dr = [2, 1, -1, -2, -2, -1, 1, 2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(l, r1, c1, r2, c2):
    queue = deque()
    queue.append((r1, c1, 0))
    visit = [[0] * l for _ in range(l)]
    visit[r1][c1] = 1

    while queue:
        r, c, step = queue.popleft()
        if r == r2 and c == c2:
            return step
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            if nr in range(l) and nc in range(l):
                if not visit[nr][nc]:
                    visit[nr][nc] = 1
                    queue.append((nr, nc, step + 1))


for _ in range(int(input())):
    l = int(input())
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    print(bfs(l, r1, c1, r2, c2))