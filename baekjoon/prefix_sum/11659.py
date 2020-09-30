from .. import util

example = """
5 3
5 4 3 2 1
1 3
2 4
5 5
"""
util.setinput(example)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

sum = [0 for _ in range(N + 1)]
nums = list(map(int, input().split()))

prev = 0
for n in range(N):
    sum[n + 1] = sum[n] + nums[n]

for _ in range(M):
    i, j = map(int, input().split())
    print(sum[j] - sum[i - 1])
