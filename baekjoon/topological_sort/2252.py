import io
import sys

example = """
32000 2
1 3
2 3
"""
sys.stdin = io.StringIO(example.strip())

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

indegrees = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegrees[B] += 1

queue = deque()
for n in range(1, N + 1):
    if indegrees[n] == 0:
        queue.append(n)

ret = []
while queue:
    cur = queue.popleft()
    ret.append(cur)

    for e in graph[cur]:
        indegrees[e] -= 1
        if indegrees[e] == 0:
            queue.append(e)

print(" ".join(map(str, ret)))
