INF = 100


def get_small_dist(dist, visited, size):
    min = None
    cur = 0
    for v in range(size):
        if min == None:
            min = dist[v]
            cur = v
        elif dist[v] < min and v not in visited:
            min = dist[v]
            cur = v
    return cur


def dijkstra(graph, start):
    size = len(graph)
    visited = []
    dist = [INF] * size

    for i in range(size):
        dist[i] = graph[start][i]
    visited.append(start)

    for i in range(size - 2):
        cur = get_small_dist(dist, visited, size)
        visited.append(cur)

        for j in range(size):
            if j in visited:
                if dist[cur] + graph[cur][j] < dist[j]:
                    dist[j] = dist[cur] + graph[cur][j]

    return dist


if __name__ == "__main__":
    graph = [
        [0, 2, 5, 1, INF, INF],
        [2, 0, 3, 2, INF, INF],
        [5, 3, 0, 3, 1, 5],
        [1, 2, 3, 0, 1, INF],
        [INF, INF, 1, 1, 0, 2],
        [INF, INF, 5, INF, 2, 0]
    ]

    print("--- dijkstra ---")
    dists = dijkstra(graph, 0)
    for idx, dist in enumerate(dists):
        print("{}: {}".format(idx, dist))
