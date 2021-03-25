import io
import sys

example = """
6 3
3 1 4 3
4 6 2 5 4
2 3 2
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import collections

if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    indegrees = [0 for _ in range(N + 1)]

    for _ in range(M):
        n, *order = map(int, input().split())

        for i in range(n - 1):
            a, b = order[i], order[i + 1]

            graph[a].append(b)
            indegrees[b] += 1

    queue = collections.deque()

    for idx in range(1, N + 1):
        if not indegrees[idx]:
            queue.append(idx)

    ret = []
    while queue:
        cur = queue.popleft()
        ret.append(cur)

        for next in graph[cur]:
            indegrees[next] -= 1
            if not indegrees[next]:
                queue.append(next)

    if len(ret) == N:
        print("\n".join(map(str, ret)))
    else:
        print(0)