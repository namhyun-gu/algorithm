import io
import sys

example = """
4
4 4
5 2
11 5
15 10
25 10
"""
sys.stdin = io.StringIO(example.strip())

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())

stations = []
for _ in range(N):
    a, b = map(int, input().split())
    heappush(stations, (a, b))

L, P = map(int, input().split())

ret = 0
temp = []
while P < L:
    while stations and P >= stations[0][0]:
        heappush(temp, -stations[0][1])
        heappop(stations)

    if not temp:
        ret = -1
        break

    P += -temp[0]
    ret += 1
    heappop(temp)

print(ret)