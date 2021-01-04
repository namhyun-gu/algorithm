import io
import sys

example = """
5
132 392 311 351 231
392 351 132 311 231
"""
sys.stdin = io.StringIO(example.strip())

# ! PyPy3로 제출해야 통과했음
# ? Ref: https://hooongs.tistory.com/118
import sys
from math import log2, ceil

input = sys.stdin.readline

N = int(input())
A = input().split()
B = {}
for idx, num in enumerate(input().split()):
    B[num] = idx

H = ceil(log2(N))
tree = [0 for _ in range(1 << H + 1)]


def update(index, diff=1, node=1, start=0, end=N - 1):
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


ret = 0
for a in A:
    num_idx = B[a]
    ret += sum(num_idx, N - 1)
    update(num_idx)

print(ret)