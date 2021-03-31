from .. import util

example = """
2
3 3 1
1 2 2
1 3 4
2 3 1
3 1 3
3 2 1
1 2 3
2 3 4
3 1 8
"""
util.setinput(example)

import sys
input = sys.stdin.readline


def bellman_ford(graph, n):
    dists = [1e9] * (n + 1)  # math.inf는 안됨 이거때매 한시간 걸림
    dists[1] = 0
    possible = False
    for k in range(n):
        for i in range(1, n + 1):
            for v, t in graph[i]:
                if dists[v] > dists[i] + t:
                    dists[v] = dists[i] + t
                    if k == n - 1:
                        possible = True
    return possible


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append((E, T))
        graph[E].append((S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((E, -T))

    if bellman_ford(graph, N):
        print("YES")
    else:
        print("NO")
