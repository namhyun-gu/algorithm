import io
import sys

example = """
5 2 2
1
2
3
4
5
1 3 0
2 2 5
1 3 6
2 2 5
"""
sys.stdin = io.StringIO(example.strip())

import sys
from math import log2, ceil

input = sys.stdin.readline

N, M, K = map(int, input().split())

nums = [int(input()) for _ in range(N)]
tree = [0 for _ in range(1 << ceil(log2(N)) + 1)]


def init(node=1, start=0, end=N - 1):
    if start == end:
        tree[node] = nums[start]
    else:
        mid = (start + end) // 2
        l = init(node * 2, start, mid)
        r = init(node * 2 + 1, mid + 1, end)
        tree[node] = (l * r) % 1000000007
    return tree[node]


def update(index, val, node=1, start=0, end=N - 1):
    if index < start or index > end:
        return

    if start == end:
        tree[node] = val
    else:
        mid = (start + end) // 2
        update(index, val, node * 2, start, mid)
        update(index, val, node * 2 + 1, mid + 1, end)

        l = tree[node * 2]
        r = tree[node * 2 + 1]
        tree[node] = (l * r) % 1000000007


def product(left, right, node=1, start=0, end=N - 1):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    l = product(left, right, node * 2, start, mid)
    r = product(left, right, node * 2 + 1, mid + 1, end)
    return (l * r) % 1000000007


init()

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        update(b, c)
    else:
        print(product(b - 1, c - 1))
