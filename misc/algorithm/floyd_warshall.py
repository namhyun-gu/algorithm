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


def floyd_warshall() -> List[List[int]]:
    vertex_size = len(graph)
    w = [[0 for i in range(vertex_size)] for j in range(vertex_size)]
    for i in range(vertex_size):
        for j in range(vertex_size):
            w[i][j] = graph[i][j]

    for k in range(vertex_size):
        for i in range(vertex_size):
            for j in range(vertex_size):
                w[i][j] = min(w[i][j], w[i][k] + w[k][j])
    return w


if __name__ == "__main__":
    print("--- floyd_warshall ---")
    dists = floyd_warshall()
    for i in range(len(dists)):
        for j in range(len(dists)):
            print(dists[i][j], end="\t")
        print()
