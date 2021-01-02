import io
import sys

example = """
10 4
75
30
100
38
50
51
52
20
81
5
1 10
3 5
6 9
8 10
"""
sys.stdin = io.StringIO(example.strip())

import sys
from math import log2, ceil

input = sys.stdin.readline

N, M = map(int, input().split())

nums = [int(input()) for _ in range(N)]

H = ceil(log2(N))
tree = [0] * (1 << H + 1)


def min_max(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (min(a[0], b[0]), max(a[1], b[1]))


def init_tree(node=1, start=0, end=N - 1):
    if start == end:
        tree[node] = (nums[start], nums[start])
    else:
        mid = (start + end) // 2
        l = init_tree(node * 2, start, mid)
        r = init_tree(node * 2 + 1, mid + 1, end)
        tree[node] = min_max(l, r)
    return tree[node]


def search(left, right, node=1, start=0, end=N - 1):
    if left > end or right < start:
        return (1000000001, 0)
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    l = search(left, right, node * 2, start, mid)
    r = search(left, right, node * 2 + 1, mid + 1, end)
    return min_max(l, r)


init_tree()

for _ in range(M):
    a, b = map(int, input().split())

    ret = search(a - 1, b - 1)
    print(ret[0], ret[1])