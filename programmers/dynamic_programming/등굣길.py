import collections


def solution(m, n, puddles):
    board = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for puddle in puddles:
        c, r = puddle
        board[r][c] = 1

    cnt = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    cnt[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i - 1][j] != 1:
                cnt[i][j] += cnt[i - 1][j]
            if board[i][j - 1] != 1:
                cnt[i][j] += cnt[i][j - 1]

    return cnt[n][m] % 1000000007