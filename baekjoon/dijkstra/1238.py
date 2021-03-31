from .. import util

example = """
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
"""
util.setinput(example)

# x -> n의 최단거리와 *역방향 그래프를 이용하여 n -> x의 최단거리를 구하면 해결할 수 있다.

from math import inf
import heapq

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
graph_r = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    graph_r[e].append((s, t))


def dijkstra(graph, start):
    dists = [inf] * len(graph)
    dists[start] = 0

    queue = []
    heapq.heappush(queue, (start, 0))

    while queue:
        u, cur_dist = heapq.heappop(queue)
        if dists[u] < cur_dist:
            continue

        for e, t in graph[u]:
            if dists[u] + t < dists[e]:
                dists[e] = dists[u] + t
                heapq.heappush(queue, (e, dists[e]))
    return dists


dists = dijkstra(graph, X)  # x -> n
dists_r = dijkstra(graph_r, X)  # n -> x

max_dist = 0
for idx in range(1, N + 1):
    max_dist = max(max_dist, dists[idx] + dists_r[idx])

print(max_dist)
