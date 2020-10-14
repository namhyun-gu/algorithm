from .. import util

example = """
6 2 10 3
"""
util.setinput(example)

import sys

input = sys.stdin.readline

x, y, w, h = map(int, input().split())

print(min(x, w - x, h - y, y))