from .. import util

example = """
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1
"""
util.setinput(example)

# 분류에 브루트포스라 모양을 추가하여 계산했는데 DFS를 쓴다고한다. (T 모양 제외)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))

tetrominos = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # I
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],  # O
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # L
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 0)],
    [(0, 0), (1, 0), (2, 0), (0, 1)],  # J
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(2, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],  # S
    [(0, 1), (0, 2), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],  # Z
    [(1, 0), (2, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],  # T
    [(0, 1), (1, 1), (2, 1), (1, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(1, 0), (1, 1), (1, 2), (0, 1)],
]


def put_tetromino(tetromino, x, y):
    sum = 0
    for tx, ty in tetromino:
        dx = x + tx
        dy = y + ty

        if dx >= M or dy >= N:
            return 0

        sum += paper[dy][dx]
    return sum


max_sum = 0
for y in range(N):
    for x in range(M):
        for tetromino in tetrominos:
            max_sum = max(max_sum, put_tetromino(tetromino, x, y))


print(max_sum)
