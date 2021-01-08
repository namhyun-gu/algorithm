import io
import sys

example = """
7
1
5
2
10
-99
7
5
"""
sys.stdin = io.StringIO(example.strip())

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())

min_heap = []
max_heap = []

for _ in range(N):
    num = int(input())

    if len(min_heap) == len(max_heap):
        heappush(max_heap, (-num, num))
    else:
        heappush(min_heap, (num, num))

    if min_heap and max_heap[0][1] > min_heap[0][1]:
        maximum = heappop(max_heap)[1]
        minimum = heappop(min_heap)[1]

        heappush(min_heap, (maximum, maximum))
        heappush(max_heap, (-minimum, minimum))

    print(max_heap[0][1])
