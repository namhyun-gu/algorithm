import io
import sys

example = """
1 1 1
2 2 2
10 4 6
50 50 50
-1 7 18
-1 -1 -1
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

memo = dict()


def w(a, b, c):
    if (a, b, c) in memo:
        return memo[(a, b, c)]

    ret = 0

    if a <= 0 or b <= 0 or c <= 0:
        ret = 1
    elif a > 20 or b > 20 or c > 20:
        ret = w(20, 20, 20)
    elif a < b and b < c:
        ret = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        ret = (
            w(a - 1, b, c)
            + w(a - 1, b - 1, c)
            + w(a - 1, b, c - 1)
            - w(a - 1, b - 1, c - 1)
        )

    memo[(a, b, c)] = ret
    return ret


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    ret = w(a, b, c)
    print(f"w({a}, {b}, {c}) = {ret}")