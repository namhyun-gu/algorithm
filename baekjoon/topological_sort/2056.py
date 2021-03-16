import io
import sys

example = """
7
5 0
1 1 1
3 1 2
6 1 1
1 2 2 4
8 2 2 4
4 3 3 5 6
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
            if durations[next] < durations[current] + temp[next]:
                durations[next] = durations[current] + temp[next]

            indegrees[next] -= 1
            if indegrees[next] == 0:
                queue.append(next)

    result = 0
    for vertex in range(1, len(durations)):
        if durations[vertex] > result:
            result = durations[vertex]

    return result


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())

    graph = [[] for _ in range(N + 1)]
    indegrees = [0 for _ in range(N + 1)]
    durations = [0 for _ in range(N + 1)]

    for n in range(1, N + 1):
        duration, _, *deps = map(int, input().split())
        durations[n] = duration

        for dep in deps:
            graph[dep].append(n)
            indegrees[n] += 1

    result = topological_sort(graph, indegrees, durations)
    print(result)
