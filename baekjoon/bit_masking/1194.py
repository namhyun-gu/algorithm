# region Input redirection
import io
import sys

example = """
7 8
a#c#eF.1
.#.#.#..
.#B#D###
0....F.1
C#E#A###
.#.#.#..
d#f#bF.1
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
from collections import deque


def add_key(bag, key):
    return bag | (1 << key)


def contain_key(bag, key):
    key = 1 << key
    return (bag & key) == key


def to_num(alpha):
    if "a" <= alpha <= "f":
        return ord(alpha) - ord("a")
    elif "A" <= alpha <= "F":
        return ord(alpha) - ord("A")


def all_key():
    key = 0
    for ch in "abcdef":
        key = add_key(key, ord(ch) - ord("a"))
    return key


def dir(r, c):
    dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    return map(lambda it: (r + it[0], c + it[1]), dirs)


if __name__ == "__main__":
    input = sys.stdin.readline

    R, C = map(int, input().split())

    maze = [input() for _ in range(R)]

    cur = None

    for r in range(R):
        for c in range(C):
            if maze[r][c] == "0":
                cur = (r, c)

    queue = deque()
    queue.append((*cur, 0))

    visit = [[[0 for _ in range(64)] for _ in range(C)] for _ in range(R)]
    visit[cur[0]][cur[1]][0] = 0

    ret = -1

    while queue:
        r, c, bag = queue.popleft()

        if maze[r][c] == "1":
            ret = visit[r][c][bag]
            break

        for dr, dc in dir(r, c):
            if dr not in range(R) or dc not in range(C):
                continue

            if visit[dr][dc][bag]:
                continue

            if maze[dr][dc] == "#":
                continue

            if "a" <= maze[dr][dc] <= "f":
                new_bag = add_key(bag, to_num(maze[dr][dc]))
                visit[dr][dc][new_bag] = visit[r][c][bag] + 1
                queue.append((dr, dc, new_bag))
            elif "A" <= maze[dr][dc] <= "F":
                if contain_key(bag, to_num(maze[dr][dc])):
                    visit[dr][dc][bag] = visit[r][c][bag] + 1
                    queue.append((dr, dc, bag))
            else:
                visit[dr][dc][bag] = visit[r][c][bag] + 1
                queue.append((dr, dc, bag))

    print(ret)