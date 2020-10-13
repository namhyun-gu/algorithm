from .. import util

example = """
4 42
"""
util.setinput(example)

import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())

visited = {}
queue = deque([(A, 0)])
while queue:
    current, cnt = queue.popleft()

    if current == B:
        print(cnt + 1)
        exit(0)

    if current > B:
        continue

    for next in [current * 2, (current * 10) + 1]:
        if next not in visited:
            visited[next] = 1
            queue.append((next, cnt + 1))


print(-1)