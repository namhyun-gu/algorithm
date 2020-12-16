import io
import sys

example = """
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
R, C, D = map(int, input().split())
board = [input().split() for _ in range(N)]

cnt = 0

rotate = [3, 0, 1, 2]

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
back_dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def work_cleaner(r, c, d):
    global cnt

    if board[r][c] == "1":
        return

    # 1. 현재 위치를 청소한다.
    if board[r][c] == "0":
        board[r][c] = "2"
        cnt += 1

    # 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 탐색한다.
    for _ in range(4):
        d = rotate[d]
        dr, dc = dir[d]
        nr, nc = r + dr, c + dc

        if board[nr][nc] == "0":
            work_cleaner(nr, nc, d)
            return

    br, bc = back_dir[d]
    nr, nc = r + br, c + bc

    work_cleaner(nr, nc, d)


work_cleaner(R, C, D)
print(cnt)