import heapq

inf = 1e9


def shortest_path(graph, N, start):
    dist = [inf for _ in range(N + 1)]
    dist[start] = 0

    heap = []
    for n in range(1, N + 1):
        heapq.heappush(heap, (dist[n], n))

    while heap:
        _, u = heapq.heappop(heap)

        for v, cost in graph[u]:
            alt = dist[u] + cost
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(heap, (dist[v], v))
    return dist


def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]

    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    dist = shortest_path(graph, N, 1)
    answer = 0
    for n in range(1, N + 1):
        if dist[n] != inf and dist[n] <= K:
            answer += 1
    return answer