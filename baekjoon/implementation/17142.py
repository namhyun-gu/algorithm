# region Input redirection
import io
import sys

example = """
7 3
2 0 2 0 1 1 0
0 0 1 0 1 0 0
0 1 1 1 1 0 0
2 1 0 0 0 0 2
1 0 0 0 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import itertools
import collections

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dir(r, c):
    return map(lambda it: (it[0] + r, it[1] + c), dirs)


def in_area(r, c):
    return r in range(N) and c in range(N)


def spread_virus(lab, virus):
    queue = collections.deque()
    time = [[-1 for _ in range(N)] for _ in range(N)]
    infect_space = 0
    latest_time = 0

    for v in virus:
        r, c = v
        time[r][c] = 0
        queue.append(v)

    while queue:
        r, c = queue.popleft()

        for dr, dc in dir(r, c):
            if not in_area(dr, dc):
                continue

            if lab[dr][dc] == 1 or time[dr][dc] != -1:
                continue

            time[dr][dc] = time[r][c] + 1
            if lab[dr][dc] == 0:
                infect_space += 1
                latest_time = time[dr][dc]

            queue.append((dr, dc))

    return latest_time, infect_space


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())

    lab = []
    virus = []
    total_space = 0

    for r in range(N):
        lab.append([])
        for c, val in enumerate(map(int, input().split())):
            lab[r].append(val)
            if val == 0:
                total_space += 1
            elif val == 2:
                virus.append((r, c))

    min_time = sys.maxsize
    for pick_virus in itertools.combinations(virus, M):
        time, infect_space = spread_virus(lab, pick_virus)
        if infect_space == total_space:
            min_time = min(min_time, time)

    print(min_time if min_time != sys.maxsize else -1)