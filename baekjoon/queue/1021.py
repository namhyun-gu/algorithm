import io
import sys

example = """
32 6
27 16 30 11 6 23
"""
sys.stdin = io.StringIO(example.strip())

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

queue = deque([*range(1, N + 1)])


def left():
    n = queue.popleft()
    queue.append(n)


def right():
    n = queue.pop()
    queue.appendleft(n)


cnt = 0
for m in map(int, input().split()):
    idx = queue.index(m)
    while m != queue[0]:
        if idx < len(queue) - idx:
            left()
            cnt += 1
        else:
            right()
            cnt += 1
    queue.popleft()

print(cnt)