# region Input redirection
import io
import sys

example = """
4 2 3
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
3 1
1 1 1 2
1 2 3 2
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
from collections import deque

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def can_visit(r, c, space):
    return r in range(N) and c in range(N) and space[r][c] == 0


def calculate_dist(space, driver_r, driver_c):
    queue = deque()
    queue.append((driver_r, driver_c))

    dist = [[0] * N for _ in range(N)]
    dist[driver_r][driver_c] = 1

    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if can_visit(nr, nc, space) and not dist[nr][nc]:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    return dist


def find_closest_guest(space, driver, guests, select, fuel):
    dist = calculate_dist(space, *driver)

    guest_with_dist = []
    for idx, guest in enumerate(guests):
        if select[idx]:
            continue

        guest_dist = dist[guest[0]][guest[1]] - 1
        guest_with_dist.append((guest_dist, *guest, idx))

        if fuel < guest_dist or guest_dist == -1:
            return None

    return sorted(guest_with_dist)[0]


def move_guest(space, driver, guest, fuel):
    dist = calculate_dist(space, *driver)
    dest_dist = dist[guest[0]][guest[1]] - 1

    if fuel < dest_dist or dest_dist == -1:
        return -1
    return dest_dist


def solution(space, driver, guests, fuel):
    select = [False] * len(guests)

    for _ in range(M):
        select_guest = find_closest_guest(space, driver, guests, select, fuel)
        if not select_guest:
            return -1

        dist, src_r, src_c, dest_r, dest_c, idx = select_guest
        driver = src_r, src_c
        fuel -= dist

        select[idx] = True

        dest_dist = move_guest(space, driver, (dest_r, dest_c), fuel)

        if dest_dist != -1:
            driver = dest_r, dest_c
            fuel += dest_dist
        else:
            return -1
    return fuel


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M, fuel = map(int, input().split())

    space = [[*map(int, input().split())] for _ in range(N)]
    driver = [*map(lambda i: int(i) - 1, input().split())]
    guests = [[*map(lambda i: int(i) - 1, input().split())] for idx in range(M)]

    print(solution(space, driver, guests, fuel))