from .. import util

example = """
6 5
1 2
2 5
5 1
3 4
4 6
"""
util.setinput(example)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
conn = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 1


def dfs(idx):
    if conn[idx] != 0:
        return

    conn[idx] = cnt
    for v in graph[idx]:
        if conn[v] == 0:
            dfs(v)


for idx in range(1, N + 1):
    if conn[idx] == 0:
        dfs(idx)
        cnt += 1

print(cnt - 1)
