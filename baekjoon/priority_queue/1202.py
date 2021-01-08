import io
import sys

example = """
3 2
1 65
5 23
2 99
10
2
"""
sys.stdin = io.StringIO(example.strip())

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, K = map(int, input().split())

jewelry = sorted([[*map(int, input().split())] for _ in range(N)])
bags = sorted([int(input()) for _ in range(K)])
index, ret, heap = 0, 0, []

for bag in bags:
    while index < N and jewelry[index][0] <= bag:
        heappush(heap, -jewelry[index][1])
        index += 1

    if heap:
        ret += -heappop(heap)

print(ret)
