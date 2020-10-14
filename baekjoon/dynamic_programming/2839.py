from .. import util

example = """
12
"""
util.setinput(example)

import sys

input = sys.stdin.readline

MAX = 10 ** 4
N = int(input())
dp = [MAX for _ in range(5001)]

dp[3] = 1
dp[5] = 1

for idx in range(6, N + 1):
    dp[idx] = min(dp[idx - 3], dp[idx - 5]) + 1

if dp[N] >= MAX:
    print(-1)
else:
    print(dp[N])
