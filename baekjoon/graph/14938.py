from .. import util

example = """
5 5 4
5 7 8 2 3
1 4 5
5 2 4
3 2 3
1 2 3
"""
util.setinput(example)

import sys

input = sys.stdin.readline

MAX = 10 ** 7
N, M, R = map(int, input().split())
items = list(map(int, input().split()))

graph = [[MAX for _ in range(N + 1)] for _ in range(N + 1)]

for r in range(R):
    s, e, w = map(int, input().split())
    graph[s][e] = w
    graph[e][s] = w


def floyd_warshall():
    w = [[MAX for _ in range(N + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            w[i][j] = graph[i][j]

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                w[i][j] = min(w[i][j], w[i][k] + w[k][j])
    return w


dists = floyd_warshall()
max_cnt = 0
for i in range(1, N + 1):
    cnt = items[i - 1]
    for j in range(1, N + 1):
        if i == j:
            continue

        if dists[i][j] <= M:
            cnt += items[j - 1]
    max_cnt = max(max_cnt, cnt)

print(max_cnt)