import io
import sys

example = """
4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import collections


def coord_string(r, c):
    return f"{r},{c}"


def find_open_boards(world, low, end):
    open_boards = collections.defaultdict(list)

    for r in range(N):
        for c in range(N):
            for nr, nc in [(r + 1, c), (r, c + 1)]:
                if nr in range(N) and nc in range(N):
                    if abs(world[r][c] - world[nr][nc]) in range(low, end + 1):
                        open_boards[coord_string(r, c)].append((nr, nc))
                        open_boards[coord_string(nr, nc)].append((r, c))
    return open_boards


def find_union(open_boards, r, c):
    union = []
    queue = collections.deque([(r, c)])
    visit = set([(r, c)])

    while queue:
        cur_r, cur_c = queue.popleft()
        cur = coord_string(cur_r, cur_c)
        union.append((cur_r, cur_c))

        if cur in open_boards:
            for open_board in open_boards[cur]:
                if open_board not in visit:
                    visit.add(open_board)
                    queue.append(open_board)
    return union


def sum_union(world, unions):
    sum = 0
    for r, c in unions:
        sum += world[r][c]
    return sum


def update_union(world, unions, value):
    for r, c in unions:
        world[r][c] = value


if __name__ == "__main__":
    input = sys.stdin.readline

    N, L, R = map(int, input().split())

    world = [[*map(int, input().split())] for _ in range(N)]

    ret = 0
    while True:
        open_boards = find_open_boards(world, L, R)
        moves = False
        visit = set()
        for r in range(N):
            for c in range(N):
                if (r, c) in visit:
                    continue

                unions = find_union(open_boards, r, c)
                for union in unions:
                    visit.add(union)

                if len(unions) >= 2:
                    moves = True
                    sum = sum_union(world, unions)
                    update_union(world, unions, (sum // len(unions)))

        if moves:
            ret += 1
        else:
            break
    print(ret)
