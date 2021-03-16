import io
import sys

example = """
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import collections


def topological_sort(graph, indegrees, durations):
    queue = collections.deque()
    temp = [*durations]

    for vertex in range(1, len(indegrees)):
        if not indegrees[vertex]:
            queue.append(vertex)

    while queue:
        current = queue.popleft()

        for next in graph[current]:
            durations[next] = max(durations[next], durations[current] + temp[next])

            indegrees[next] -= 1
            if not indegrees[next]:
                queue.append(next)

    return durations


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())

    graph = [[] for _ in range(N + 1)]
    indegrees = [0 for _ in range(N + 1)]
    durations = [0 for _ in range(N + 1)]

    for n in range(1, N + 1):
        duration, *deps = map(int, input().split()[:-1])
        durations[n] = duration

        for dep in deps:
            graph[dep].append(n)
            indegrees[n] += 1

    result = topological_sort(graph, indegrees, durations)
    for vertex in range(1, N + 1):
        print(result[vertex])