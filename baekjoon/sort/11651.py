from .. import util

example = """
5
0 4
1 2
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
    coords.append((y, x))

for coord in sorted(coords):
    y, x = coord
    print(x, y)