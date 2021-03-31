# %%
import sys


def bellman_ford(graph, start):
    vertex_size = len(graph)

    # 시작 지점에서 다른 정점까지의 거리를 아직 모르기에 최대 값으로 저장한다.
    # 시작 지점에서의 거리는 0으로 초기화한다.
    dist = [inf] * vertex_size
    dist[start] = 0

    # 시작 지점에서 최단 거리 경로의 이전 정점을 저장하는 배열로,
    # 초기에는 Null로 초기화한다.
    prev = [None] * vertex_size

    # 그래프에서 모든 간선을 구한다.
    edges = get_edges(graph)

    # 모든 간선에 대해 최단거리를 갱신하는 과정을 (정점 개수 - 1)만큼 반복한다.
    for _ in range(vertex_size - 1):
        for u, v in edges:
            # 시작 -> v의 거리보다,
            # 시작 -> u -> v로 가는 거리 중 가까운 거리로
            # 시작 -> v를 갱신한다.
            #
            # 이때 시작 -> u -> v가 가깝다면,
            # v로 방문하는 이전 정점을 u로 갱신한다.
            if dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                prev[v] = u

    # 모든 간선에 대해 확인하여 음수 사이클이 있는지를 확인한다.
    # 위에서 N - 1번 갱신을 진행하고 나서 또 갱신이 된다면, 음수 가중치 사이클이 존재한다.
    for u, v in edges:
        if dist[u] + graph[u][v] < dist[v]:
            # 음수 가중치 사이클 존재!
            pass

    return dist, prev


def get_edges(graph):
    vertex_size = len(graph)

    # 가중치가 존재하는 모든 간선을 구한다.
    edges = []
    for i in range(vertex_size):
        for j in range(vertex_size):
            if graph[i][j] != inf:
                edges.append((i, j))
    return edges


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

dist, prev = bellman_ford(graph, 1)
print(dist)
print(path(prev, 1, 3))