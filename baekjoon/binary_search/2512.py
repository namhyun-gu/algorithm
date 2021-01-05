import io
import sys

example = """
4
120 110 140 150
485
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

N = int(input())
requests = sorted([*map(int, input().split())])
budget = int(input())


def sum_requests(mid):
    sum = 0
    for request in requests:
        sum += request if request <= mid else mid
    return sum


if sum(requests) <= budget:
    print(max(requests))
else:
    ret = 0
    l, r = 0, requests[-1]
    while l <= r:
        mid = (l + r) // 2
        sum = sum_requests(mid)

        if sum > budget:
            r = mid - 1
        else:
            l = mid + 1
            ret = max(ret, mid)
    print(ret)