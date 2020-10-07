from .. import util

example = """
3
1 2 3
4 5 6
4 9 0
"""
util.setinput(example)

import sys

input = sys.stdin.readline

N = int(input())

min_window = [[0 for _ in range(3)] for _ in range(2)]
max_window = [[0 for _ in range(3)] for _ in range(2)]

for n in range(N):
    num = list(map(int, input().split()))

    current = n % 2
    next = (n + 1) % 2

    min_window[next][0] = min(
        min_window[current][0] + num[0], min_window[current][1] + num[0]
    )
    min_window[next][1] = min(
        min_window[current][0] + num[1],
        min_window[current][1] + num[1],
        min_window[current][2] + num[1],
    )
    min_window[next][2] = min(
        min_window[current][1] + num[2], min_window[current][2] + num[2]
    )

    max_window[next][0] = max(
        max_window[current][0] + num[0], max_window[current][1] + num[0]
    )
    max_window[next][1] = max(
        max_window[current][0] + num[1],
        max_window[current][1] + num[1],
        max_window[current][2] + num[1],
    )
    max_window[next][2] = max(
        max_window[current][1] + num[2], max_window[current][2] + num[2]
    )

print(max(max_window[N % 2]), min(min_window[N % 2]))