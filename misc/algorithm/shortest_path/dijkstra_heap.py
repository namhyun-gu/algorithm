from math import inf
from typing import List
import heapq

graph: List[List[int]] = [
    [0, 7, inf, inf, 3, 10, inf],
    [7, 0, 4, 10, 2, 6, inf],
    [inf, 4, 0, 2, inf, inf, inf],
    [inf, 10, 2, 0, 11, 9, 4],
    [3, 2, inf, 11, 0, inf, 5],
    [10, 6, inf, 9, inf, 0, inf],
    [inf, inf, inf, 4, 5, inf, 0],
]


def dijkstra_heap(start: int) -> List[int]:
    vertext_size = len(graph)
    dist = [inf] * vertext_size
    queue = []

    dist[start] = 0

    heapq.heappush(queue, (start, 0))

    while queue:
        u, cur_dist = heapq.heappop(queue)
        if dist[u] < cur_dist:
            continue

        for v in range(vertext_size):
            if dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                heapq.heappush(queue, (v, dist[v]))
    return dist


if __name__ == "__main__":
    print("--- dijkstra_heap ---")
    dists = dijkstra_heap(0)
    for idx, dist in enumerate(dists):
        print("{}: {}".format(idx, dist))
