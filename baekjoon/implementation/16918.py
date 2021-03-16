import io
import sys

example = """
6 7 0
.......
...O...
....O..
.......
OO.....
OO.....
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def save_bomb(board):
    bomb = []

    for r, line in enumerate(board):
        for c, ch in enumerate(line):
            if ch == "O":
                bomb.append((r, c))
    return bomb


def fill_bomb(r, c):
    return [["O" for _ in range(c)] for _ in range(r)]


def bomb_target(bomb):
    r, c = bomb
    return [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]


def explode_bomb(board, bombs):
    R, C = len(board), len(board[0])
    for bomb in bombs:
        r, c = bomb
        board[r][c] = "."
        for target_r, target_c in bomb_target(bomb):
            if target_r in range(R) and target_c in range(C):
                board[target_r][target_c] = "."
    return board


if __name__ == "__main__":
    input = sys.stdin.readline

    R, C, N = map(int, input().split())
    N -= 2

    board = [input().rstrip() for _ in range(R)]
    count = 0
    while count <= N:
        if count % 2 == 0:
            bombs = save_bomb(board)
            board = fill_bomb(R, C)
        else:
            board = explode_bomb(board, bombs)
        count += 1

    for line in board:
        print("".join(line))
