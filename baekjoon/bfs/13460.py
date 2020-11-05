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
이 문제를 처음 풀 때 빨간색 구슬과 파란색 구슬이 동시에 움직인다고 하여

tilt_board() 라는 함수를 만들고 이 안에서 빨간색과 파란색 구슬이
한 칸씩 동시에 이동하고
문제의 조건에 따라 이동한 구슬 위치를 사용할지를 결정하도록 했다.

위 방식대로 작성을 하니 빨간 구슬이 구멍에 들어갔을 떄,
파란 구슬도 구멍에 들어간 경우에 대한 예외처리를 하지 못 했고
문제를 푸는데 시간이 오래 걸려 풀이를 참고하였다.

참고한 풀이에서는 각 구슬을 벽 이전 혹은 구멍까지 이동하도록 하였고
이동한 거리를 반환하여 이동한 거리가 적은 구슬이 이전 위치로 가도록 하였다.

참고한 풀이를 통해 제출을 하였을 떈 92% 가량에서 런타임 에러가 발생했었는데
visit를 4차원 배열로 작성할 때 문제가 발생하는 것이라 생각이 되어

visit를 일차원 배열로 작성하고, 각 구슬의 위치를 배열로 넣도록 한 뒤,
방문 여부를 확인할 때 구슬 위치가 담긴 배열이 있는지를 확인하는 방법으로 작성하니
통과할 수 있었다.

Ref: https://rebas.kr/725
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
                print(count + 1)
                return

            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx - tx, nry - ty
                else:
                    nbx, nby = nbx - tx, nby - ty

            if [nrx, nry, nbx, nby] not in visit:
                visit.append([nrx, nry, nbx, nby])
                queue.append((nrx, nry, nbx, nby, count + 1))
    print(-1)


bfs(rx, ry, bx, by)