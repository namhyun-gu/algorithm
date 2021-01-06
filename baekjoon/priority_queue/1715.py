import io
import sys

example = """
3
10
20
40
"""
sys.stdin = io.StringIO(example.strip())

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    heappush(heap, int(input()))

ret = 0
while len(heap) > 1:
    first = heappop(heap)
    second = heappop(heap)
    ret += first + second
    heappush(heap, first + second)

print(ret)
