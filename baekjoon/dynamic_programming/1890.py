# region Input redirection
import io
import sys

example = """
4
2 3 3 1
1 2 1 3
1 2 3 1
3 1 1 0
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    board = [[*map(int, input().split())] for _ in range(N)]
    dp = [[0] * N for _ in range(N)]

    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if dp[i][j] == 0 or (i == N - 1 and j == N - 1):
                continue

            dist = board[i][j]

            if i + dist < N:
                dp[i + dist][j] += dp[i][j]

            if j + dist < N:
                dp[i][j + dist] += dp[i][j]

    print(dp[N - 1][N - 1])
