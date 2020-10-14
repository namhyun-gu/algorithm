from .. import util

example = """
3 1000000
"""
util.setinput(example)

import sys

input = sys.stdin.readline

M, N = map(int, input().split())

sieve = [1 for _ in range(N + 1)]
sieve[0] = sieve[1] = 0

m = int(N ** 0.5)
for i in range(2, m + 1):
    if sieve[i]:
        for j in range(i + i, N + 1, i):
            sieve[j] = 0

for num in range(M, N + 1):
    if sieve[num]:
        print(num)