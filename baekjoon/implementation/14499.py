import io
import sys

example = """
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

N, M, y, x, K = map(int, input().split())
board = [[int(i) for i in input().strip().split()] for _ in range(N)]
dice_moves = [int(i) for i in input().strip().split()]
dice = [0 for _ in range(7)]

moves = [0, (1, 0), (-1, 0), (0, -1), (0, 1)]

rolls = [
    0,
    [0, 4, 2, 1, 6, 5, 3],
    [0, 3, 2, 6, 1, 5, 4],
    [0, 5, 1, 3, 4, 6, 2],
    [0, 2, 6, 3, 4, 1, 5],
]


def roll_dice(dir: int):
    global dice

    new_dice = dice[:]
    roll = rolls[dir]
    for idx in range(1, 7):
        new_dice[idx] = dice[roll[idx]]
    dice = new_dice


def move_dice(dir: int) -> bool:
    global x, y

    dx, dy = moves[dir]
    nx, ny = x + dx, y + dy

    if nx in range(M) and ny in range(N):
        x = nx
        y = ny
        return True
    else:
        return False


def update_dice():
    if board[y][x] == 0:
        board[y][x] = dice[6]
    else:
        dice[6], board[y][x] = board[y][x], 0


for dice_move in dice_moves:
    if move_dice(dice_move):
        roll_dice(dice_move)
        update_dice()
        print(dice[1])
