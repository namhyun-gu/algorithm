from math import inf
from typing import List

graph: List[List[int]] = [
    [0, 7, inf, inf, 3, 10, inf],
    [7, 0, 4, 10, 2, 6, inf],
    [inf, 4, 0, 2, inf, inf, inf],
    [inf, 10, 2, 0, 11, 9, 4],
    [3, 2, inf, 11, 0, inf, 5],
    [10, 6, inf, 9, inf, 0, inf],
    [inf, inf, inf, 4, 5, inf, 0],
]


def get_min_dist(dist: List[int], visited: List[int]):
    min = (inf, -1)

    for v in range(len(graph)):
        if v not in visited and dist[v] < min[0]:
            min = (dist[v], v)

    return min[1]


def dijkstra(start: int) -> List[int]:
    vertext_size = len(graph)
    visited = [start]
    dist = [inf] * vertext_size

    for v in range(vertext_size):
        dist[v] = graph[start][v]
    dist[start] = 0

    for i in range(vertext_size - 2):
        u = get_min_dist(dist, visited)
        visited.append(u)
        for v in range(vertext_size):
            if v not in visited and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
    return dist


if __name__ == "__main__":
    print("--- dijkstra ---")
    dists = dijkstra(0)
    for idx, dist in enumerate(dists):
        print("{}: {}".format(idx, dist))
