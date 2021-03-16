import io
import sys

example = """
5
-99 -2 -1 4 98
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    liquid = [*map(int, input().split())]

    total = 10e9
    l, r = 0, N - 1
    result = 0, 0
    while l < r:
        sum = liquid[l] + liquid[r]
        if abs(sum) < total:
            total = abs(sum)
            result = liquid[l], liquid[r]
        elif sum < 0:
            l += 1
        else:
            r -= 1

    print(result[0], result[1])
