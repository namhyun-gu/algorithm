# region Input redirection
import io
import sys

example = """
8 17
...XXXXXX..XX.XXX
....XXXXXXXXX.XXX
...XXXXXXXXXXXX..
..XXXXX.LXXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXXL...
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
from collections import deque

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def melt_and_meet(lake: list, water: deque, swan: deque):
    swan_b = swan.pop()

    day = 1
    while swan:
        temp = deque()

        # Melt
        while water:
            r, c = water.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if nr in range(R) and nc in range(C):
                    if lake[nr][nc] == "X":
                        lake[nr][nc] = "."
                        temp.append((nr, nc))

        water = temp

        # Meet
        temp = deque()
        while swan:
            swan_a = swan.popleft()
            r, c = swan_a

            if swan_a == swan_b:
                return day

            if lake[r][c] == "L":
                lake[r][c] = day

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if nr in range(R) and nc in range(C):
                    if lake[nr][nc] == "." or lake[nr][nc] == "L":
                        lake[nr][nc] = day
                        swan.append((nr, nc))
                        temp.append((nr, nc))

        swan = temp
        day += 1
    return day


if __name__ == "__main__":
    input = sys.stdin.readline

    R, C = map(int, input().split())

    lake = []
    water = deque()
    swan = deque()

    for r in range(R):
        lake.append([*input().rstrip()])

        for c in range(C):
            if lake[r][c] == "L":
                swan.append((r, c))
                water.append((r, c))
            elif lake[r][c] == ".":
                water.append((r, c))

    print(melt_and_meet(lake, water, swan))