from .. import util

example = """
6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6
"""
util.setinput(example)

import sys
from heapq import heappush, heappop
from collections import deque
input = sys.stdin.readline

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

N = int(input())
space = [[0 for _ in range(N)] for _ in range(N)]

babe_shark_pos = None
babe_shark_size = 2

for y in range(N):
    line = list(map(int, input().split()))
    for x in range(N):
        if line[x] == 9:  # 상어 위치는 비어있어야함
            babe_shark_pos = (x, y)
        else:
            space[y][x] = line[x]


def is_valid(x, y):
    return x >= 0 and x < N and y >= 0 and y < N


def bfs():
    shark_x, shark_y = babe_shark_pos
    queue = deque([babe_shark_pos])
    dists = [[-1 for _ in range(N)] for _ in range(N)]

    dists[shark_y][shark_x] = 0
    min_dist = []

    while queue:
        x, y = queue.popleft()

        if space[y][x] != 0 and space[y][x] < babe_shark_size:
            heappush(min_dist, (dists[y][x], y, x))

        for dx, dy in dirs:
            tx, ty = (x + dx, y + dy)

            if not is_valid(tx, ty):
                continue

            if dists[ty][tx] == -1 and space[ty][tx] <= babe_shark_size:
                dists[ty][tx] = dists[y][x] + 1
                queue.append((tx, ty))
    if min_dist:
        return min_dist[0]
    else:
        return None


time = 0
eat = 0
while True:
    min_fish = bfs()
    if min_fish is None:
        break

    dist, y, x = min_fish
    time += dist

    eat += 1
    # 크기만큼 먹어야 커진다는 걸 못 봐서 오래 걸림
    if babe_shark_size == eat:
        babe_shark_size += 1
        eat = 0
    babe_shark_pos = (x, y)
    space[y][x] = 0

print(time)
