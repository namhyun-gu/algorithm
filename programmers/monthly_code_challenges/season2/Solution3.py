import collections


def find_leaf(graph):
    leaf = []
    for v, edge in enumerate(graph):
        if len(edge) == 1:
            leaf.append(v)
    return leaf


def solution(a, edges):
    if sum(a) != 0:
        return -1

    graph = [set() for _ in range(len(a))]
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    answer = 0
    queue = collections.deque(find_leaf(graph))

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if a[u] != 0:
                answer += abs(a[u])
                a[v] += a[u]
                a[u] = 0
            graph[u] = {}
            graph[v].remove(u)

            if len(graph[v]) == 1:
                queue.append(v)

    return answer


if __name__ == "__main__":
    ret = solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]])
    print(ret)

    ret = solution([0, 1, 0], [[0, 1], [1, 2]])
    print(ret)