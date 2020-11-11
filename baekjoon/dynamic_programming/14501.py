from .. import util

example = """
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
"""
util.setinput(example)

import sys

input = sys.stdin.readline

N = int(input())
DP = [0] * (N + 2)
T, P = [0] * (N + 1), [0] * (N + 1)

for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

for i in range(1, N + 2):
    for j in range(i):
        DP[i] = max(DP[i], DP[j])

        if j + T[j] == i:
            DP[i] = max(DP[i], DP[j] + P[j])

print(max(DP))
