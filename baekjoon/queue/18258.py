import io
import sys

example = """
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
"""
sys.stdin = io.StringIO(example.strip())

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()

for _ in range(N):
    op, *num = input().split()
    if num:
        num = int(num[0])
    if op == "push":
        queue.append(num)
    elif op == "pop":
        print(queue.popleft() if queue else -1)
    elif op == "size":
        print(len(queue))
    elif op == "empty":
        print(0 if queue else 1)
    elif op == "front":
        print(queue[0] if queue else -1)
    elif op == "back":
        print(queue[-1] if queue else -1)