from .. import util

example = """
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
"""
util.setinput(example)

import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())
lab = [[0 for _ in range(M)] for _ in range(N)]
viruses = []
blank = []
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for n in range(N):
    line = list(map(int, input().split()))
    for m in range(M):
        if line[m] == 2:
            viruses.append((m, n))
        elif line[m] == 0:
            blank.append((m, n))
        lab[n][m] = line[m]


def calc_safe(lab):
    cnt = 0
    for n in range(N):
        for m in range(M):
            if lab[n][m] == 0:
                cnt += 1
    return cnt


def spread_virus(wall_fits):
    new_lab = [[0 for _ in range(M)] for _ in range(N)]
    for n in range(N):
        for m in range(M):
            new_lab[n][m] = lab[n][m]

    for wx, wy in wall_fits:
        new_lab[wy][wx] = 1

    queue = list(viruses)
    while queue:
        vx, vy = queue.pop()
        for dx, dy in dirs:
            tx = vx + dx
            ty = vy + dy

            if tx < 0 or ty < 0 or tx >= M or ty >= N:
                continue

            if new_lab[ty][tx] == 0:
                new_lab[ty][tx] = 2
                queue.append((tx, ty))

    return calc_safe(new_lab)


max_area = 0
for wall_fits in itertools.combinations(blank, 3):
    safe = spread_virus(wall_fits)
    max_area = max(max_area, safe)
print(max_area)
