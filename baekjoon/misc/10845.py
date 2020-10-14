from .. import util

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
util.setinput(example)

import sys

input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    op, *param = input().rstrip().split()
    if op == "push":
        queue.append(int(param[0]))
    elif op == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif op == "size":
        print(len(queue))
    elif op == "empty":
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