import io
import sys

example = """
4
5
20
10
20
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

N = int(input())
ropes = sorted([int(input()) for _ in range(N)], reverse=True)

ret = 0
for n in range(1, N + 1):
    minimum = ropes[n - 1]
    ret = max(ret, minimum * n)

print(ret)
