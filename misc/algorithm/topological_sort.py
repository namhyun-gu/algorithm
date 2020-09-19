from typing import List

graph: List[List[int]] = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0]
]


def topological_sort():
    vertext_size = len(graph)
    indegrees = [0] * vertext_size

    for cur in range(vertext_size):
        for v in range(vertext_size):
            if graph[cur][v]:
                indegrees[v] += 1

    queue = []
    for idx, indegree in enumerate(indegrees):
        if not indegree:
            queue.append(idx)

    while queue:
        print("queue: {}".format(queue))
        cur = queue.pop(0)
        for v in range(vertext_size):
            if graph[cur][v]:
                print("{} - - -> {}".format(cur, v))
                indegrees[v] -= 1
                if not indegrees[v]:
                    queue.append(v)
            else:
                print("{} - x -> {}".format(cur, v))


if __name__ == "__main__":
    print("--- topological_sort ---")
    topological_sort()
