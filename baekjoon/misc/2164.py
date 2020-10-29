from .. import util

example = """
6
"""
util.setinput(example)

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()

for n in range(N):
    queue.append(n + 1)

while len(queue) > 1:
    queue.popleft()
    top = queue.popleft()
    queue.append(top)

print(queue[0])
