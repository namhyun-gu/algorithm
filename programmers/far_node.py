from collections import deque


def bfs(graph, start):
    visited = [0] * len(graph)
    visited[start] = 1
    dists = [1e5] * len(graph)
    dists[start] = 0
    # 큐로 이용할때 리스트에서 pop(0)은 O(n)이므로 deque 이용
    queue = deque([(0, start)])
    while queue:
        dist, cur = queue.popleft()
        for v in graph[cur]:
            if not visited[v]:
                visited[v] = 1
                queue.append((dist + 1, v))
            dists[v] = min(dists[v], dist + 1)
    return dists[1:]


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)

    dists = bfs(graph, 1)
    max_dist = max(dists)
    far_nodes = list(
        filter(lambda node: node[1] == max_dist, enumerate(dists)))
    return len(far_nodes)


if __name__ == "__main__":
    assert solution(6, [[3, 6], [4, 3], [3, 2], [1, 3],
                        [1, 2], [2, 4], [5, 2]]) == 3
