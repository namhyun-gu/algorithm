# region Input redirection
import io
import sys

example = """
6 1
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def is_same_height(board):
    for i in range(1, N):
        if board[0] != board[i]:
            return False
    return True


def can_way(board):
    if is_same_height(board):
        return True

    slopes = [0 for _ in range(N)]

    for i in range(N - 1):
        diff = board[i] - board[i + 1]
        if diff == 1:  # 2 -> 1
            if can_slope(board, slopes, i + 1):
                set_slope(slopes, i + 1)
            else:
                return False
        elif diff == -1:  # 1 -> 2
            if can_slope(board, slopes, i, reverse=True):
                set_slope(slopes, i, reverse=True)
            else:
                return False
        elif abs(diff) > 1:
            return False
    return True


def set_slope(slopes, i, reverse=False):
    if reverse:
        for l in range(L):
            slopes[i - l] = 2
    else:
        for l in range(L):
            slopes[i + l] = 1


def can_slope(board, slopes, i, reverse=False):
    if reverse:
        if i - L + 1 not in range(N):
            return False

        for l in range(L):
            if board[i] != board[i - l]:
                return False

            if slopes[i - l] != 0:
                return False
    else:
        if i + L - 1 not in range(N):
            return False

        for l in range(L):
            if board[i] != board[i + l]:
                return False

            if slopes[i + l] != 0:
                return False
    return True


if __name__ == "__main__":
    input = sys.stdin.readline

    N, L = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]
    board_r = list(zip(*board[::-1]))

    result = 0

    for i in range(N):
        if can_way(board[i]):
            result += 1

        if can_way(board_r[i]):
            result += 1

    print(result)