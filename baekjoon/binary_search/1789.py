import io
import sys

example = """
200
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

S = int(input())

l, r = 1, 4294967295
while l <= r:
    mid = (l + r) // 2
    if (mid * (mid - 1)) // 2 > S:
        r = mid - 1
    else:
        l = mid + 1

print(r - 1)