from .. import util

example = """
4
3
0
4
0
"""
util.setinput(example)

import sys
input = sys.stdin.readline

K = int(input())

stack = []
for _ in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

sum = 0
for num in stack:
    sum += num
print(sum)