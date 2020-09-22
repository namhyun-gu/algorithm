from .. import util

example = """
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
"""
util.setinput(example)

import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)


def bfs(start):
    queue = [start]
    visited = [0] * (N + 1)
    visited[start] = 1
    parent = [0] * (N + 1)
    while queue:
        cur = queue.pop()
        for next in graph[cur]:
            # if next not in visited: O(n) 이라 시간초과
            if not visited[next]:
                parent[next] = cur
                visited[next] = 1
                queue.append(next)
    return parent


parent = bfs(1)
for idx in range(2, len(parent)):
    print(parent[idx])
