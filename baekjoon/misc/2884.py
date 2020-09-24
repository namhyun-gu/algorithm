from .. import util

example = """
23 40
"""
util.setinput(example)

import sys
input = sys.stdin.readline

H, M = map(int, input().split())

time = (H * 60) + M
time -= 45

if time < 0:
    time = (24 * 60) + time

H = int(time / 60)
M = time - (H * 60)
print(H, M)
