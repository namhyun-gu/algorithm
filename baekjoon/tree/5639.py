from .. import util

example = """
50
30
24
5
28
45
98
52
60
"""
util.setinput(example)

import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

node = []
while True:
    try:
        node.append(int(input().rstrip()))
    except:
        break


def post_order(start, end):
    if (end - start) < 0:
        return

    root = node[start]
    right_start = end + 1
    for idx in range(start + 1, end + 1):
        n = node[idx]
        if n > root:
            right_start = idx
            break

    post_order(start + 1, right_start - 1)
    post_order(right_start, end)
    print(root)


post_order(0, len(node) - 1)