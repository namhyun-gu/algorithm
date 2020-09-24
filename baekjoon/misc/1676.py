from .. import util

example = """
10
"""
util.setinput(example)

import sys
input = sys.stdin.readline

N = int(input())


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


cnt = 0
for c in str(factorial(N))[::-1]:
    if c != '0':
        break
    cnt += 1
print(cnt)
