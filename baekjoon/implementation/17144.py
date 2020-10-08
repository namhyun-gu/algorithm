from .. import util

example = """
7 8 2
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
"""
util.setinput(example)

import sys

input = sys.stdin.readline

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cleaner = []

R, C, T = map(int, input().split())
house = [[0 for _ in range(C)] for _ in range(R)]

for r in range(R):
    line = list(map(int, input().split()))
    for c in range(C):
        if line[c] == -1:
            cleaner.append(r)
        house[r][c] = line[c]


def is_cleaner(r, c):
    return r in cleaner and c == 0


def is_valid(r, c):
    return r >= 0 and r < R and c >= 0 and c < C and not is_cleaner(r, c)


def spread(cur_house, r, c):
    if is_cleaner(r, c):
        return

    valid = []
    for dc, dr in dirs:
        tc = c + dc
        tr = r + dr

        if is_valid(tr, tc):
            valid.append((tc, tr))

    amount = house[r][c] // 5
    for tc, tr in valid:
        cur_house[tr][tc] = cur_house[tr][tc] + amount

    cur_house[r][c] = cur_house[r][c] + house[r][c] - (amount * len(valid))


def run_cleaner(house, start, reverse):
    if reverse:
        for r in range(start - 1, 0, -1):
            house[r][0] = house[r - 1][0]

        for c in range(C - 1):
            house[0][c] = house[0][c + 1]

        for r in range(0, start):
            house[r][C - 1] = house[r + 1][C - 1]

        for c in range(C - 1, 1, -1):
            house[start][c] = house[start][c - 1]
    else:
        for r in range(start + 1, R - 1):
            house[r][0] = house[r + 1][0]

        for c in range(C - 1):
            house[R - 1][c] = house[R - 1][c + 1]

        for r in range(R - 1, start, -1):
            house[r][C - 1] = house[r - 1][C - 1]

        for c in range(C - 1, 1, -1):
            house[start][c] = house[start][c - 1]

    house[start][1] = 0


def do_space(house, func):
    for r in range(R):
        for c in range(C):
            func(house, r, c)


def sum_dust():
    result = 0
    for r in range(R):
        result += sum(house[r])
    return result


def create_house():
    return [[0 for _ in range(C)] for _ in range(R)]


for _ in range(T):
    new_house = create_house()
    do_space(new_house, spread)
    run_cleaner(new_house, cleaner[0], reverse=True)
    run_cleaner(new_house, cleaner[1], reverse=False)
    house = new_house.copy()

house[cleaner[0]][0] = 0
house[cleaner[1]][0] = 0
print(sum_dust())