from .. import util

example = """
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""
util.setinput(example)

import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(N)] for _ in range(N)]
triangle = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        triangle[i][j] = line[j]

dp[0][0] = triangle[0][0]
for i in range(1, N):
    for j in range(N):
        if j == 0:
            dp[i][j] = triangle[i][j] + dp[i - 1][j]
        else:
            dp[i][j] = triangle[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[N - 1]))
