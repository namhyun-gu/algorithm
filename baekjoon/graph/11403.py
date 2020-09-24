from .. import util

example = """
7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
"""
util.setinput(example)

import sys
input = sys.stdin.readline

N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        graph[i][j] = line[j]


def floyd_warshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = max(graph[i][j], graph[i][k] and graph[k][j])


floyd_warshall()

for i in range(N):
    for j in range(N):
        print(graph[i][j], end=" ")
    print()
