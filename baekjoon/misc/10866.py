from .. import util

example = """
22
front
back
pop_front
pop_back
push_front 1
front
pop_back
push_back 2
back
pop_front
push_front 10
push_front 333
front
back
pop_back
pop_back
push_back 20
push_back 1234
front
back
pop_back
pop_back
"""
util.setinput(example)

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()
for _ in range(N):
    op, *param = input().rstrip().split()
    if op == "push_front":
        queue.appendleft(int(param[0]))
    elif op == "push_back":
        queue.append(int(param[0]))
    elif op == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif op == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif op == "size":
        print(len(queue))
    elif op == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif op == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif op == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])