# %%
import sys


# Dijkstra은 음의 가중치가 없는 그래프의 한 정점에서 모든 정점까지의 최단거리를 구하는 알고리즘이다.
# O(V^2)의 시간복잡도를 가진다.
# 우선순위 큐(힙)을 이용하면 O((V + E)logV)의 시간복잡도를 가진다.
def dijkstra(graph, start):
    vertex_size = len(graph)

    # 시작 지점에서 다른 정점까지의 거리를 아직 모르기에 최대 값으로 저장한다.
    # 시작 지점에서의 거리는 0으로 초기화한다.
    dist = [inf] * vertex_size
    dist[start] = 0

    # 시작 지점에서 최단 거리 경로의 이전 정점을 저장하는 배열로,
    # 초기에는 Null로 초기화한다.
    prev = [None] * vertex_size

    # 모든 정점을 Set에 추가한다.
    vertex_set = set()
    for v in range(vertex_size):
        vertex_set.add(v)

    while vertex_set:
        # Set 중에서 거리가 가장 가까운 정점을 가져오고, 해당 정점을 Set에서 제거한다.
        u = min_dist(vertex_set, dist)
        vertex_set.remove(u)

        # 가져온 정점에서 이동 가능한 (이웃) 정점들을 반복한다.
        # 해당 정점이 Set에 있는지를 확인한다.
        for v in neighbor(graph, u):
            if v in vertex_set:
                # 시작 -> v의 거리보다,
                # 시작 -> u -> v로 가는 거리 중 가까운 거리로
                # 시작 -> v를 갱신한다.
                #
                # 이때 시작 -> u -> v가 가깝다면,
                # v로 방문하는 이전 정점을 u로 갱신한다.
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
                    prev[v] = u

    return dist, prev


# Set의 정점들 중에서 가장 가까이 있는 정점을 구한다.
def min_dist(vertex_set, dist):
    min_dist = inf
    u = None

    for v in vertex_set:
        if dist[v] < min_dist:
            min_dist = dist[v]
            u = v

    return u


# v에서 이동 가능한 모든 이웃을 구한다.
def neighbor(graph, v):
    neighbor = []
    for u, w in enumerate(graph[v]):
        if w != inf:
            neighbor.append(u)
    return neighbor


import heapq

# * 앞서 작성한 O(V^2) 인 Dijkstra보다 우선순위를 사용한 Dijkstra가 간결하고 성능이 좋으므로
# * 이를 사용하는 것을 권장한다.

# 위 Dijkstra에서 최소 거리의 정점을 가져올 때 우선순위 큐를 사용하여 성능을 개선한 버전이다.
# O(V^2) 에서 O((V + E)logV)의 시간복잡도를 가진다.
def dijkstra_priority_queue(graph, start):
    vertex_size = len(graph)

    # 시작 지점에서 다른 정점까지의 거리를 아직 모르기에 최대 값으로 저장한다.
    # 시작 지점에서의 거리는 0으로 초기화한다.
    dist = [inf] * vertex_size
    dist[start] = 0

    # 시작 지점에서 최단 거리 경로의 이전 정점을 저장하는 배열로,
    # 초기에는 Null로 초기화한다.
    prev = [None] * vertex_size

    # 모든 정점을 Heap에 추가한다.
    # 우선순위 기준은 거리로, 최소 거리인 정점이 앞에 온다.
    heap = []
    for v in range(vertex_size):
        heapq.heappush(heap, (dist[v], v))

    while heap:
        # 최소 거리인 정점을 가져온다.
        _, u = heapq.heappop(heap)

        # 가져온 정점에서 이동 가능한 (이웃) 정점들을 반복한다.
        for v in neighbor(graph, u):
            # 시작 -> v의 거리보다,
            # 시작 -> u -> v로 가는 거리 중 가까운 거리로
            # 시작 -> v를 갱신한다.
            #
            # 이때 시작 -> u -> v가 가깝다면,
            # v로 방문하는 이전 정점을 u로 갱신한다.
            # 동시에 Heap에 최소 거리로 갱신된 v를 추가한다.
            alt = dist[u] + graph[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

                heapq.heappush(heap, (alt, v))

    return dist, prev


# 경로는 역순으로 나오기에, source -> target이 필요하다면
# 역순인 경로를 뒤집어서 구할 수 있다.
def path(prev, source, target):
    path = []
    # 끝 정점부터 시작한다.
    u = target
    # 현재 정점에서 이전 정점이 있을때만 반복한다.
    while prev[u]:
        # 이전 정점을 경로에 추가한다.
        path.append(u)
        # 이전 정점을 현재 정점으로 갱신한다.
        u = prev[u]
    # 경로에 시작 정점을 추가한다.
    path.append(source)
    return path


inf = sys.maxsize

graph = [
    [0, 7, inf, inf, 3, 10, inf],
    [7, 0, 4, 10, 2, 6, inf],
    [inf, 4, 0, 2, inf, inf, inf],
    [inf, 10, 2, 0, 11, 9, 4],
    [3, 2, inf, 11, 0, inf, 5],
    [10, 6, inf, 9, inf, 0, inf],
    [inf, inf, inf, 4, 5, inf, 0],
]

dist, prev = dijkstra(graph, 1)
print(dist)
print(path(prev, 1, 3))

dist, prev = dijkstra_priority_queue(graph, 1)
print(dist)
print(path(prev, 1, 3))
# %%
