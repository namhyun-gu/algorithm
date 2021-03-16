import io
import sys

example = """
4 2
4 2
3 1
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
from heapq import heappush, heappop


def topological_sort(graph, indegrees):
    queue = []

    for vertex in range(1, len(indegrees)):
        if not indegrees[vertex]:
            heappush(queue, vertex)

    order = []
    solved = [False for _ in range(len(graph))]

    while queue:
        current = heappop(queue)
        solved[current] = True
        order.append(current)

        for next in graph[current]:
            indegrees[next] -= 1
            if not indegrees[next]:
                heappush(queue, next)

    for vertex in range(1, len(graph)):
        if not solved[vertex]:
            order.append(vertex)

    return order


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    indegrees = [0 for _ in range(N + 1)]

    for _ in range(M):
        A, B = map(int, input().split())

        graph[A].append(B)
        indegrees[B] += 1

    result = topological_sort(graph, indegrees)
    print(" ".join(map(str, result)))