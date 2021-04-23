import io
import sys

example = """
6 7
1 2 1
1 4 3
3 6 1
4 5 1
2 3 2
3 4 1
5 6 2
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import heapq

inf = sys.maxsize


def dijkstra(graph, N, start):
    dist = [inf for _ in range(N + 1)]
    dist[start] = 0

    prev = [None for _ in range(N + 1)]

    heap = []
    for v in range(1, N + 1):
        heapq.heappush(heap, (dist[v], v))

    while heap:
        _, u = heapq.heappop(heap)

        for v, w in enumerate(graph[u]):
            if w == inf:
                continue

            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

                heapq.heappush(heap, (dist[v], v))
    return dist, prev


def path(prev, start, dest):
    path = []
    u = dest

    while prev[u]:
        path.append(u)
        u = prev[u]
    path.append(start)
    return path


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())

    graph = [[inf for _ in range(N + 1)] for _ in range(N + 1)]

    edges = []

    for _ in range(M):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

        graph[u][v] = w
        graph[v][u] = w

    dist, prev = dijkstra(graph, N, 1)
    shortest = dist[N]
    shortest_path = path(prev, 1, N)

    answer = inf

    for i in range(len(shortest_path) - 1):
        u, v = shortest_path[i], shortest_path[i + 1]

        w = graph[u][v]

        graph[u][v] = inf
        graph[v][u] = inf

        dist, _ = dijkstra(graph, N, 1)
        if dist[N] != inf and dist[N] > shortest:
            if answer == inf:
                answer = dist[N] - shortest
            else:
                answer = max(answer, dist[N] - shortest)

        graph[u][v] = w
        graph[v][u] = w

    if answer == inf:
        print(-1)
    else:
        print(answer)