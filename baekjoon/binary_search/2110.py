import io
import sys

example = """
5 3
1
2
8
4
9
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

N, C = map(int, input().split())
houses = sorted([int(input()) for _ in range(N)])


def count_wifi(mid):
    start, cnt = houses[0], 1

    for i in range(1, N):
        dist = houses[i] - start
        if mid <= dist:
            start = houses[i]
            cnt += 1
    return cnt


if C == 2:
    print(houses[-1] - houses[0])
else:
    ret = 0
    l, r = 1, houses[-1] - houses[0]
    while l <= r:
        mid = (l + r) // 2
        cnt = count_wifi(mid)

        if cnt < C:
            r = mid - 1
        else:
            l = mid + 1
            ret = mid
    print(ret)