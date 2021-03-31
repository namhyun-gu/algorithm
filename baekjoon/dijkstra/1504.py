from .. import util

example = """
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3
"""
util.setinput(example)

import sys
import math
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start):
    dists = [math.inf] * (N + 1)
    dists[start] = 0
    queue = []

    heapq.heappush(queue, (0, start))
    while queue:
        dist, u = heapq.heappop(queue)
        for v, w in graph[u]:
            if dists[v] > dist + w:
                dists[v] = dist + w
                heapq.heappush(queue, (dists[v], v))
    return dists


start = dijkstra(1)
dist1 = dijkstra(v1)
dist2 = dijkstra(v2)

dist = min(start[v1] + dist1[v2] + dist2[N], start[v2] + dist2[v1] + dist1[N])
if dist == math.inf:
    print(-1)
else:
    print(dist)
