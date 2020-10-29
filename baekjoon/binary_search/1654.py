from .. import util

example = """
1 1
1
"""
util.setinput(example)

import sys

input = sys.stdin.readline

K, N = map(int, input().split())

lines = []
for _ in range(K):
    lines.append(int(input()))

lines = sorted(lines)


def cut_line_count(size):
    sum = 0
    for line in lines:
        sum += line // size
    return sum


left = 1
right = lines[-1]

result = 0
while left <= right:
    mid = (left + right) // 2
    cnt = cut_line_count(mid)
    if cnt < N:
        right = mid - 1
    else:
        result = max(result, mid)
        left = mid + 1

print(result)
