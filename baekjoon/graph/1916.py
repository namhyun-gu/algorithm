from .. import util

example = """
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
"""
util.setinput(example)

import sys
import math
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e, w))

S, E = map(int, sys.stdin.readline().split())


def dijkstra(start):
    dists = [math.inf] * (N + 1)
    dists[start] = 0
    queue = []

    heapq.heappush(queue, (0, start))

    while queue:
        cur_dist, u = heapq.heappop(queue)
        for v, w in graph[u]:
            if cur_dist + w < dists[v]:
                dists[v] = cur_dist + w
                heapq.heappush(queue, (dists[v], v))
    return dists


print(dijkstra(S)[E])
