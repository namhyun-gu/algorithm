from .. import util

example = """
6
0 0 0 0 0 0
0 1 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
"""
util.setinput(example)

"""
Ref: https://buddev.tistory.com/36

dp[행][열][방향]을 선언한 후 (방향: 가로 - 0, 세로 - 1, 대각선 - 2)

dp[r][c][방향] = (r, c) 칸에 방향으로 놓을 수 있는 방법
따라서 결과는 (n, n) 칸에 모든 방향으로 놓을 수 있는 방법을 더해 구할 수 있다.

dp[r][c][가로] = dp[r][c - 1][가로] + dp[r][c - 1][대각선]
> 가로 방향으로 오는 경우는 왼쪽 열에 가로, 대각선으로 오는 경우만 있다.

dp[r][c][세로] = dp[r - 1][c][세로] + dp[r - 1][c][대각선]
> 세로 방향으로 오는 경우는 위쪽 행에 세로, 대각선으로 오는 경우만 있다.

dp[r][c][대각선] =
    dp[r - 1][c - 1][가로] + dp[r - 1][c - 1][세로] + dp[r - 1][c - 1][대각선]
> 대각선 방향으로 오는 경우는 왼쪽 위에 모든 방향으로 오는 경우가 있다.
"""
import sys

input = sys.stdin.readline

N = int(input())

house = [[0 for _ in range(N)] for _ in range(N)]
for r in range(N):
    line = list(map(int, input().split()))
    for c in range(N):
        house[r][c] = line[c]

dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]

dp[0][1][0] = 1

for r in range(N):
    for c in range(2, N):
        if house[r][c] == 1:
            continue

        dp[r][c][0] = dp[r][c - 1][0] + dp[r][c - 1][2]

        if r == 0:
            continue

        dp[r][c][1] = dp[r - 1][c][1] + dp[r - 1][c][2]

        if house[r - 1][c] == 0 and house[r][c - 1] == 0:
            for i in range(3):
                dp[r][c][2] += dp[r - 1][c - 1][i]


N -= 1
print(dp[N][N][0] + dp[N][N][1] + dp[N][N][2])