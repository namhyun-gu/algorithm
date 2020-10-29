from .. import util

example = """
7 3
"""
util.setinput(example)

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque()

for n in range(N):
    queue.append(n + 1)

result = []
while queue:
    for k in range(K):
        if k < K - 1:
            queue.append(queue.popleft())
        else:
            result.append(queue.popleft())

arr = ", ".join(map(str, result))
print(f"<{arr}>")