import io
import sys

example = """
3 3
0 0 0
0 4 0
0 0 0
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


def cctv_dirs(cctv_type):
    if cctv_type in [1, 3, 4]:
        return [0, 1, 2, 3]
    elif cctv_type in [2]:
        return [0, 1]
    return [0]


def cctv_mark_dirs(cctv_type):
    if cctv_type == 1:
        return [[UP], [DOWN], [LEFT], [RIGHT]]
    elif cctv_type == 2:
        return [[UP, DOWN], [LEFT, RIGHT]]
    elif cctv_type == 3:
        return [[UP, RIGHT], [RIGHT, DOWN], [LEFT, DOWN], [UP, LEFT]]
    elif cctv_type == 4:
        return [
            [UP, LEFT, RIGHT],
            [UP, RIGHT, DOWN],
            [LEFT, RIGHT, DOWN],
            [LEFT, UP, DOWN],
        ]
    elif cctv_type == 5:
        return [[UP, LEFT, RIGHT, DOWN]]


def dfs(cctv, select, depth=0):
    global cases

    if depth == len(cctv):
        cases.append(list(select))
        return

    type, _, _ = cctv[depth]
    for dir in cctv_dirs(type):
        select.append((cctv[depth], dir))
        dfs(cctv, select, depth + 1)
        select.pop()


def run_case(room, case):
    global min_cnt

    for cctv, dir in case:
        mark_cctv_range(room, cctv, dir)
        cnt = calculate_blind(room)
        min_cnt = min(min_cnt, cnt)


def mark_cctv_range(room, cctv, dir):
    cctv_type, row, col = cctv
    mark_dirs = [mark_cctv_up, mark_cctv_down, mark_cctv_left, mark_cctv_right]
    for mark_dir in cctv_mark_dirs(cctv_type)[dir]:
        mark_dirs[mark_dir](room, row, col)


def calculate_blind(room):
    cnt = 0
    for r in range(len(room)):
        for c in range(len(room[0])):
            if room[r][c] == 0:
                cnt += 1
    return cnt


def mark_cctv_up(room, row, col):
    for r in range(row - 1, -1, -1):
        if r not in range(len(room)):
            break

        if room[r][col] == 6:
            break
        room[r][col] = "#"


def mark_cctv_down(room, row, col):
    for r in range(row + 1, len(room)):
        if r not in range(len(room)):
            break

        if room[r][col] == 6:
            break
        room[r][col] = "#"


def mark_cctv_left(room, row, col):
    for c in range(col - 1, -1, -1):
        if c not in range(len(room[0])):
            break

        if room[row][c] == 6:
            break
        room[row][c] = "#"


def mark_cctv_right(room, row, col):
    for c in range(col + 1, len(room[0])):
        if c not in range(len(room[0])):
            break

        if room[row][c] == 6:
            break
        room[row][c] = "#"


def copy_room(room):
    new = []
    for col in range(len(room)):
        line = []
        for row in room[col]:
            line.append(row)
        new.append(line)
    return new


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())

    room = []
    cctv = []
    min_cnt = 0

    for n in range(N):
        line = [*map(int, input().split())]
        for m in range(M):
            if line[m] in range(1, 6):
                cctv.append((line[m], n, m))
            # CCTV가 없는 경우를 고려하여 빈 공간을 미리 구함
            elif line[m] == 0:
                min_cnt += 1
        room.append(line)

    cases = []
    dfs(cctv, [])
    for case in cases:
        copied_room = copy_room(room)
        run_case(copied_room, case)

    print(min_cnt)