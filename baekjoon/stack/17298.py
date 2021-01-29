import io
import sys

example = """
4
3 5 2 7
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

N = int(input())
nums = [*map(int, input().split())]

ret = [-1] * N

stack = [0]

for i in range(1, N):
    num = nums[i]
    while stack and nums[stack[-1]] < num:
        ret[stack[-1]] = num
        stack.pop()
    stack.append(i)

print(" ".join(map(str, ret)))
