from os import cpu_count
from .. import util

example = """
5 17
"""
util.setinput(example)

# Ref: 0-1 BFS (https://justicehui.github.io/medium-algorithm/2018/08/30/01BFS/)

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque([N])
dist = [-1 for _ in range(100001)]
dist[N] = 0

while queue:
    current = queue.popleft()
    if current == K:
        break

    if current * 2 <= 100000 and dist[current * 2] == -1:
        dist[current * 2] = dist[current]
        queue.appendleft(current * 2)

    if current - 1 >= 0 and dist[current - 1] == -1:
        dist[current - 1] = dist[current] + 1
        queue.append(current - 1)

    if current + 1 <= 100000 and dist[current + 1] == -1:
        dist[current + 1] = dist[current] + 1
        queue.append(current + 1)

print(dist[K])
