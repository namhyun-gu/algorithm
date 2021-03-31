# %%
import sys


# Floyd Warshall은 음의 가중치를 갖는 경우에도 사용할 수 있는 최단거리 계산 알고리즘이다.
# O(V^3)의 시간복잡도를 가지기에 크기가 작은 경우에 적합하다.
def floyd_warshall(graph):
    vertex_size = len(graph)
    # 최단 거리를 기록하기 위해 배열을 만들고, 그래프 내용대로 초기화한다.
    dist = [[graph[i][j] for j in range(vertex_size)] for i in range(vertex_size)]

    for k in range(vertex_size):
        for i in range(vertex_size):
            for j in range(vertex_size):
                # i -> j 의 거리와, i -> k -> j 의 거리 중 가까운 거리를 i -> j 의 거리로 저장한다.
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


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

floyd_warshall(graph)
# %%
import sys

# Floyd Warshall에 최단거리 경로를 구하기 위한 함수이다.
def floyd_warshall_with_path_reconstruction(graph):
    vertex_size = len(graph)

    dist = [[0 for _ in range(vertex_size)] for _ in range(vertex_size)]

    # 초기값은 u -> v 로 갈 수 있는 경로가 없다는 Null 과 같은 값이 되어야한다.
    next = [[None for _ in range(vertex_size)] for _ in range(vertex_size)]

    # 최단 거리를 기록하기 위해 배열을 만들고, 그래프 내용대로 초기화한다.
    for u in range(vertex_size):
        for v in range(vertex_size):
            dist[u][v] = graph[u][v]
            # u -> v 로 이동할 수 있으면, u -> v 로 가기위한 u 에서의 다음 경로는 v 임을 저장한다.
            if dist[u][v] != inf:
                next[u][v] = v

    for k in range(vertex_size):
        for i in range(vertex_size):
            for j in range(vertex_size):
                # i -> j 의 거리와, i -> k -> j 의 거리 중 가까운 거리를 i -> j 의 거리로 저장한다.
                #
                # 이때 i -> j 보다 i -> k 가 더 가까우므로,
                # i -> j 로 가는 경로를 i -> k 로 업데이트한다.
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]

    return dist, next


def path(next, u, v):
    # u -> v로 이동할 수 있는지 확인하고 그렇지 않다면 빈 경로를 반환한다.
    if next[u][v] == None:
        return []

    path = [u]
    while u != v:
        # u -> v 로 가기위한 다음 위치를 u에 저장하고 경로에 추가한다.
        #
        # e.g 1 -> 3 경로를 구할 때 1 -> 3에 2가 저장되어있다면,
        #     u는 2로 갱신되고, u는 v와 같지 않기 때문에 다음 차례에
        #     2 -> 3의 경로를 가져와 갱신한다.
        u = next[u][v]
        path.append(u)
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

dist, next = floyd_warshall_with_path_reconstruction(graph)

print(dist)
path(next, 1, 3)
# %%
