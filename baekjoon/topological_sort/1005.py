import io
import sys

example = """
5
3 2
1 2 3
3 2
2 1
1
4 3
5 5 5 5
1 2
1 3
2 3
4
5 10
100000 99999 99997 99994 99990
4 5
3 5
3 4
2 5
2 4
2 3
1 5
1 4
1 3
1 2
4
4 3
1 1 1 1
1 2
3 2
1 4
4
7 8
0 0 0 0 0 0 0
1 2
1 3
2 4
3 4
4 5
4 6
5 7
6 7
7
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

    for v in range(1, len(indegrees)):
        if not indegrees[v]:
            queue.append(v)

    while queue:
        cur = queue.popleft()

        for next in graph[cur]:
            durations[next] = max(durations[next], durations[cur] + temp[next])

            indegrees[next] -= 1
            if not indegrees[next]:
                queue.append(next)

    return durations


if __name__ == "__main__":
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())
        graph = [[] for _ in range(N + 1)]
        indegrees = [0 for _ in range(N + 1)]
        durations = [0, *map(int, input().split())]

        for _ in range(K):
            x, y = map(int, input().split())
            graph[x].append(y)
            indegrees[y] += 1

        target = int(input())
        result = topological_sort(graph, indegrees, durations)
        print(result[target])