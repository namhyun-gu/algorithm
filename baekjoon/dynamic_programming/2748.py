from .. import util

example = """
10
"""
util.setinput(example)

import sys

input = sys.stdin.readline

N = int(input())
F = [0 for _ in range(N + 1)]
F[1] = 1

for n in range(2, N + 1):
    F[n] = F[n - 1] + F[n - 2]

print(F[N])