import io
import sys

example = """
3 3
1 2 2
3 1 3
2 3 2
1 3
"""
sys.stdin = io.StringIO(example.strip())

import sys
from collections import deque

MAX = 1e9

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, e = map(int, input().split())


def bfs(weight):
    queue = deque([s])
    visit = [0] * (N + 1)
    visit[s] = 1

    while queue:
        cur = queue.popleft()

        if cur == e:
            return True

        for next, limit in graph[cur]:
            if not visit[next] and weight <= limit:
                visit[next] = 1
                queue.append(next)

    return False


ret = 0
l, r = 1, MAX
while l <= r:
    mid = (l + r) // 2
    able = bfs(mid)

    if able:
        l = mid + 1
    else:
        r = mid - 1

print(int(r))