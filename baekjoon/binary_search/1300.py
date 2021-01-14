import io
import sys

example = """
3
7
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

N = int(input())
K = int(input())


def index(value):
    idx = 0
    for i in range(1, N + 1):
        idx += min(value // i, N)
    return idx


ret = 0
l, r = 1, N * N

while l <= r:
    mid = (l + r) // 2
    if index(mid) < K:
        l = mid + 1
    else:
        ret = mid
        r = mid - 1

print(ret)