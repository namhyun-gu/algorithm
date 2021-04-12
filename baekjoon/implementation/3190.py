import io
import sys

example = """
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import collections

dirs = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}


def rotate(dir, rotate):
    if dir == "R":
        return "U" if rotate == "L" else "D"
    elif dir == "L":
        return "D" if rotate == "L" else "U"
    elif dir == "U":
        return "L" if rotate == "L" else "R"
    elif dir == "D":
        return "R" if rotate == "L" else "L"


def contain_tail(sr, sc, tail):
    for tr, tc in tail:
        if sr == tr and tc == sc:
            return True
    return False


def move_snake(board, snake, tail, dir):
    sr, sc = snake.pop()
    dr, dc = dirs[dir]
    nr, nc = sr + dr, sc + dc

    tail.append((sr, sc))
    snake.append((nr, nc))

    if nr not in range(len(board)) or nc not in range(len(board[0])):
        return False

    if contain_tail(nr, nc, tail):
        return False

    if board[nr][nc] == "a":
        board[nr][nc] = "-"
    else:
        tail.popleft()
    return True


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    board = [["-" for _ in range(N)] for _ in range(N)]

    K = int(input())

    for _ in range(K):
        r, c = map(int, input().split())
        board[r - 1][c - 1] = "a"

    snake = []
    snake.append((0, 0))
    tail = collections.deque()
    snake_dir = "R"

    cnt = 0
    change = {}

    L = int(input())
    for _ in range(L):
        x, c = input().split()
        x = int(x)

        change[x] = c

    while True:
        cnt += 1
        if not move_snake(board, snake, tail, snake_dir):
            break

        if cnt in change:
            snake_dir = rotate(snake_dir, change[cnt])

    print(cnt)