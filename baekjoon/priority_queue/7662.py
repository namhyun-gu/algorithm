import io
import sys

example = """
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
"""
sys.stdin = io.StringIO(example.strip())

import sys
import heapq

input = sys.stdin.readline

T = int(input())


def sync(heap, contain):
    while heap and not contain[heap[0][1]]:
        heapq.heappop(heap)


def pop(heap, contain):
    if heap:
        contain[heap[0][1]] = 0
        heapq.heappop(heap)


for _ in range(T):
    contain = [0] * 1_000_001
    min_heap, max_heap = [], []

    N = int(input())
    for idx in range(N):
        op, n = input().split()
        n = int(n)

        if op == "I":
            heapq.heappush(min_heap, (n, idx))
            heapq.heappush(max_heap, (-n, idx))
            contain[idx] = 1
        elif op == "D":
            if n == 1:
                sync(max_heap, contain)
                pop(max_heap, contain)
            else:
                sync(min_heap, contain)
                pop(min_heap, contain)

    sync(max_heap, contain)
    sync(min_heap, contain)

    if max_heap and min_heap:
        print(f"{-max_heap[0][0]} {min_heap[0][0]}")
    else:
        print("EMPTY")