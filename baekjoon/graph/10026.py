from .. import util

example = """
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
"""
util.setinput(example)

import sys
from collections import deque
input = sys.stdin.readline

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N = int(input())
picture = []

for _ in range(N):
    picture.append(input())


def is_valid(x, y):
    return x >= 0 and y >= 0 and x < N and y < N


def bfs(x, y, shown, group, is_color_blind):
    color = picture[y][x]
    queue = deque([(x, y)])
    visited = [(x, y)]

    while queue:
        cur_x, cur_y = queue.popleft()
        shown[cur_y][cur_x] = group

        for dx, dy in dirs:
            tx = cur_x + dx
            ty = cur_y + dy

            if not is_valid(tx, ty) or shown[ty][tx] != 0:
                continue

            next_color = picture[ty][tx]
            if color == next_color or \
                (is_color_blind and color == 'R' and next_color == 'G') or \
                    (is_color_blind and color == 'G' and next_color == 'R'):
                if (tx, ty) not in visited:
                    queue.append((tx, ty))
                    visited.append((tx, ty))
    return group + 1


normal_shown = [[0 for _ in range(N)] for _ in range(N)]
blind_shown = [[0 for _ in range(N)] for _ in range(N)]

normal_group = 1
blind_group = 1
for y in range(N):
    for x in range(N):
        if normal_shown[y][x] == 0:
            normal_group = bfs(x, y, normal_shown, normal_group, False)
        if blind_shown[y][x] == 0:
            blind_group = bfs(x, y, blind_shown, blind_group, True)

print(normal_group - 1, blind_group - 1)
