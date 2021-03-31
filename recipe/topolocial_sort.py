# %%
import collections


def topological_sort(graph, indegrees):
    queue = collections.deque()

    # indegree가 0인 노드를 queue에 추가한다.
    for v in range(1, len(indegrees)):
        if not indegrees[v]:
            queue.append(v)

    # queue에서 노드를 가져오고,
    # 해당 노드에서 다음으로 이동할 수 있는 노드를 반복하여 indegrees를 줄여준다.
    # indegrees가 0이 된다면 큐에 추가한다.
    while queue:
        current = queue.popleft()
        print(current)

        for next in graph[current]:
            indegrees[next] -= 1
            if indegrees[next] == 0:
                queue.append(next)


N = 4

graph = [[] for _ in range(N + 1)]

#       2
# 1 ->      -> 4
#       3
edges = [(1, 2), (1, 3), (2, 4), (3, 4)]

# 각 노드의 indegree를 구한다.
indegrees = [0 for _ in range(N + 1)]

for s, e in edges:
    graph[s].append(e)
    indegrees[e] += 1

topological_sort(graph, indegrees)