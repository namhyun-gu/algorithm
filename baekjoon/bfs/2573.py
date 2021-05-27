# region Input redirection
import io
import sys

example = """
40 20
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0 
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0 
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 10 10 10 10 1 10 10 10 10 10 10 10 10 10 10 10 10 10 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
from collections import deque


def melt(arctic):
    temp = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if arctic[r][c] > 0:
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if nr not in range(R) or nc not in range(C):
                        continue

                    if arctic[nr][nc] == 0:
                        temp[r][c] += 1

    for r in range(R):
        for c in range(C):
            arctic[r][c] -= temp[r][c]
            if arctic[r][c] < 0:
                arctic[r][c] = 0


def is_seperate(arctic):
    visit = [[0 for _ in range(C)] for _ in range(R)]
    count = 0

    for r in range(R):
        for c in range(C):
            if arctic[r][c] > 0 and not visit[r][c]:
                if count > 0:
                    return True

                visit[r][c] = 1
                conn(arctic, visit, r, c)
                count += 1

    return False


def conn(arctic, visit, r, c):
    queue = deque()
    queue.append((r, c))

    while queue:
        r, c = queue.popleft()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc

            if nr not in range(R) or nc not in range(C):
                continue

            if arctic[nr][nc] == 0:
                continue

            if visit[nr][nc]:
                continue

            visit[nr][nc] = 1
            queue.append((nr, nc))


def is_all_melted(arctic):
    count = 0
    for row in arctic:
        count += sum(row)
    return count == 0


def print_arctic(arctic):
    for r in range(R):
        for c in range(C):
            print(arctic[r][c], end=" ")
        print()
    print()


if __name__ == "__main__":
    input = sys.stdin.readline

    R, C = map(int, input().split())

    arctic = [[*map(int, input().split())] for _ in range(R)]

    year = 0

    while True:
        if is_seperate(arctic):
            break

        if is_all_melted(arctic):
            print(0)
            exit()

        melt(arctic)
        year += 1

    print(year)