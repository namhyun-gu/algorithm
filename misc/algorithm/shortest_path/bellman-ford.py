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


def bellman_ford(src, dest):
    vertex_size = len(graph)
    dist = [inf] * vertex_size
    dist[src] = 0

    for k in range(vertex_size):
        for i in range(vertex_size):
            for j in range(vertex_size):
                if graph[i][j] != inf:
                    if dist[j] > dist[i] + graph[i][j]:
                        dist[j] = dist[i] + graph[i][j]

    for i in range(vertex_size):
        for j in range(vertex_size):
            if graph[i][j] != inf:
                if dist[j] > dist[i] + graph[i][j]:
                    return inf
    return dist[dest]


if __name__ == "__main__":
    print("--- bellman-ford ---")
    for src in range(len(graph)):
        for dest in range(len(graph)):
            print(bellman_ford(src, dest), end="\t")
        print()
