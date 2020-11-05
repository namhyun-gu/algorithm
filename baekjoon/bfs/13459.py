from .. import util

example = """
7 7
#######
#...RB#
#.#####
#.....#
#####.#
#O....#
#######
"""
util.setinput(example)

"""
이 문제는 구슬 탈출 2 (13460)의 출력 값을
이동한 횟수가 아닌 가능 여부만 반환하면 되는 문제이다.
"""
import sys
from collections import deque

input = sys.stdin.readline

tilts = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())

board = [list(input().strip()) for _ in range(N)]

rx, ry, bx, by = [0] * 4

for n in range(N):
    for m in range(M):
        if board[n][m] == "R":
            rx, ry = m, n
        if board[n][m] == "B":
            bx, by = m, n


def move(x, y, tx, ty):
    count = 0
    while board[y + ty][x + tx] != "#" and board[y][x] != "O":
        x += tx
        y += ty
        count += 1
    return x, y, count


def bfs(rx, ry, bx, by):
    visit = []
    queue = deque()

    visit.append([rx, ry, bx, by])
    queue.append((rx, ry, bx, by, 0))

    while queue:
        rx, ry, bx, by, count = queue.popleft()

        if count >= 10:
            break

        for tx, ty in tilts:
            nrx, nry, rc = move(rx, ry, tx, ty)
            nbx, nby, bc = move(bx, by, tx, ty)

            if board[nby][nbx] == "O":
                continue

            if board[nry][nrx] == "O":
                print(1)
                return

            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx - tx, nry - ty
                else:
                    nbx, nby = nbx - tx, nby - ty

            if [nrx, nry, nbx, nby] not in visit:
                visit.append([nrx, nry, nbx, nby])
                queue.append((nrx, nry, nbx, nby, count + 1))
    print(0)


bfs(rx, ry, bx, by)