import io
import sys

example = """
103000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000107
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def square_range(num):
    for _range in [range(0, 3), range(3, 6), range(6, 9)]:
        if num in _range:
            return _range


def check_valid(board, row, col, num):
    # Check row
    for c in range(9):
        if board[row][c] == num:
            return False

    # Check col
    for r in range(9):
        if board[r][col] == num:
            return False

    # Check square
    for r in square_range(row):
        for c in square_range(col):
            if board[r][c] == num:
                return False

    return True


def backtracking(board, blank, index):
    if index == len(blank):
        for r in range(9):
            for c in range(9):
                print(board[r][c], end="")
            print()
        exit(0)

    for num in range(1, 10):
        r, c = blank[index]

        if check_valid(board, r, c, num):
            board[r][c] = num
            backtracking(board, blank, index + 1)
            board[r][c] = 0


if __name__ == "__main__":
    input = sys.stdin.readline

    board = []
    blank = []

    for r in range(9):
        line = []
        for c, ch in enumerate(map(int, input().rstrip())):
            if ch == 0:
                blank.append((r, c))
            line.append(ch)
        board.append(line)

    backtracking(board, blank, 0)