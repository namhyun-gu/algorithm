from .. import util

example = """
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""
util.setinput(example)

import heapq
import sys
from math import inf

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))


def dijkstra(start):
    dists = [inf] * (V + 1)
    dists[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        cur_dist, u = heapq.heappop(queue)
        for v, w in graph[u]:
            if cur_dist + w < dists[v]:
                dists[v] = cur_dist + w
                heapq.heappush(queue, (dists[v], v))
    return dists[1:]


dists = dijkstra(K)
for dist in dists:
    if dist == inf:
        print("INF")
    else:
        print(dist)
