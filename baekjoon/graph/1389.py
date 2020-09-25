from .. import util

example = """
5 5
1 3
1 4
4 5
4 3
3 2
"""
util.setinput(example)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[7 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1


def floyd_warshall():
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


floyd_warshall()

queue = []
min_idx = 0
min_sum = 1e4
for i in range(1, N + 1):
    sum = 0
    for j in range(1, N + 1):
        if i != j:
            sum += graph[i][j]
    if sum < min_sum:
        min_sum = sum
        min_idx = i

print(min_idx)
