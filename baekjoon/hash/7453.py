import io
import sys

example = """
6
-45 22 42 -16
-41 -27 56 30
-36 53 -37 77
-36 30 -75 -46
26 -38 -10 62
-32 -54 -6 45
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []

for _ in range(N):
    for arr, num in zip([A, B, C, D], map(int, input().split())):
        arr.append(num)

temp = dict()
for a in A:
    for b in B:
        if (a + b) in temp:
            temp[a + b] += 1
        else:
            temp[a + b] = 1

ret = 0
for c in C:
    for d in D:
        if -(c + d) in temp:
            ret += temp[-(c + d)]

print(ret)