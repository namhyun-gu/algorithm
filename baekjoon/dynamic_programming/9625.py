from .. import util

example = """
4
"""
util.setinput(example)

import sys

input = sys.stdin.readline

K = int(input())
DP = [0] * (K + 1)
DP[0] = (1, 0)
DP[1] = (0, 1)

for k in range(2, K + 1):
    A = DP[k - 1][0] + DP[k - 2][0]
    B = DP[k - 1][1] + DP[k - 2][1]
    DP[k] = A, B

A, B = DP[K]
print(A, B)