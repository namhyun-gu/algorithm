from .. import util

example = """
2
11
11
"""
util.setinput(example)

import sys
input = sys.stdin.readline


N = int(input())
video = []

for _ in range(N):
    video.append(input())


def get_area(x, y, n):
    if n == 1:
        return [(x, y)]

    half = int(n / 2)
    return [(x, y), (x + half, y), (x, y + half), (x + half, y + half)]


def do_compress(x, y, size):
    first = video[y][x]
    for dy in range(size):
        for dx in range(size):
            if video[y + dy][x + dx] != first:
                return (False, first)
    return (True, first)


def compress(x, y, size):
    if size == 1:
        return video[y][x]

    str = "("
    areas = get_area(x, y, size)
    for ax, ay in areas:
        success, result = do_compress(ax, ay, int(size / 2))
        if success:
            str += result
        else:
            str += compress(ax, ay, int(size / 2))
    str += ")"
    return str


success, result = do_compress(0, 0, N)
if not success:
    print(compress(0, 0, N))
else:
    print(result)
