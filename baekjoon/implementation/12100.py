import io
import sys

example = """
3
2 2 2
4 4 4
8 8 8
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def copy_board(board):
    return [[board[i][j] for j in range(len(board))] for i in range(len(board))]


def move_up(board):
    for i in range(N):
        pivot = 0
        target = 0
        for j in range(N):
            if board[j][i] == 0:
                continue
            if target == 0:
                target = board[j][i]
            else:
                if target == board[j][i]:
                    board[pivot][i] = target * 2
                    target = 0
                    pivot += 1
                else:
                    board[pivot][i] = target
                    target = board[j][i]
                    pivot += 1
            board[j][i] = 0
        if target != 0:
            board[pivot][i] = target
    return board


def move_down(board):
    for i in range(N):
        pivot = N - 1
        target = 0
        for j in range(N - 1, -1, -1):
            if board[j][i] == 0:
                continue
            if target == 0:
                target = board[j][i]
            else:
                if target == board[j][i]:
                    board[pivot][i] = target * 2
                    target = 0
                    pivot -= 1
                else:
                    board[pivot][i] = target
                    target = board[j][i]
                    pivot -= 1
            board[j][i] = 0
        if target != 0:
            board[pivot][i] = target
    return board


def move_right(board):
    for i in range(N):
        pivot = N - 1
        target = 0
        for j in range(N - 1, -1, -1):
            if board[i][j] == 0:
                continue
            if target == 0:
                target = board[i][j]
            else:
                if target == board[i][j]:
                    board[i][pivot] = target * 2
                    target = 0
                    pivot -= 1
                else:
                    board[i][pivot] = target
                    target = board[i][j]
                    pivot -= 1
            board[i][j] = 0
        if target != 0:
            board[i][pivot] = target
    return board


def move_left(board):
    for i in range(N):
        pivot = 0
        target = 0
        for j in range(N):
            if board[i][j] == 0:
                continue
            if target == 0:
                target = board[i][j]
            else:
                if target == board[i][j]:
                    board[i][pivot] = target * 2
                    target = 0
                    pivot += 1
                else:
                    board[i][pivot] = target
                    target = board[i][j]
                    pivot += 1
            board[i][j] = 0
        if target != 0:
            board[i][pivot] = target
    return board


def dfs(board, depth):
    global max_num

    if depth == 5:
        for line in board:
            max_num = max(max_num, *line)
        return

    for operation in [move_up, move_down, move_left, move_right]:
        dfs(operation(copy_board(board)), depth + 1)


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    board = [[*map(int, input().split())] for _ in range(N)]

    max_num = 0
    dfs(board, 0)

    print(max_num)