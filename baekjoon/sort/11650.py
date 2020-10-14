from .. import util

example = """
5
3 4
1 1
1 -1
2 2
3 3
"""
util.setinput(example)

import sys

input = sys.stdin.readline

N = int(input())

coords = []
for _ in range(N):
    x, y = map(int, input().split())
    coords.append((x, y))

for coord in sorted(coords):
    x, y = coord
    print(x, y)