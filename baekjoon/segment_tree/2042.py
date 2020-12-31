import io
import sys

example = """
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
"""
sys.stdin = io.StringIO(example.strip())

import sys
from math import log2, ceil

input = sys.stdin.readline

N, M, K = map(int, input().split())

nums = [int(input()) for _ in range(N)]

H = ceil(log2(N))
tree = [0] * (1 << H + 1)


def init(node=1, start=0, end=N - 1):
    if start == end:
        tree[node] = nums[start]
    else:
        mid = (start + end) // 2
        l = init(node * 2, start, mid)
        r = init(node * 2 + 1, mid + 1, end)
        tree[node] = l + r
    return tree[node]


def update(index, diff, node=1, start=0, end=N - 1):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(index, diff, node * 2, start, mid)
        update(index, diff, node * 2 + 1, mid + 1, end)


def sum(left, right, node=1, start=0, end=N - 1):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    l = sum(left, right, node * 2, start, mid)
    r = sum(left, right, node * 2 + 1, mid + 1, end)
    return l + r


init()

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        diff = c - nums[b]
        nums[b] = c
        update(b, diff)
    elif a == 2:
        print(sum(b - 1, c - 1))