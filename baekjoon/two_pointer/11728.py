import io
import sys

example = """
4 3
2 3 5 9
1 4 7
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys

input = sys.stdin.readline

_ = input()
A = [*map(int, input().split())]
B = [*map(int, input().split())]

a, b = 0, 0
idx = 0
ret = [0] * (len(A) + len(B))

while a < len(A) and b < len(B):
    if A[a] < B[b]:
        ret[idx] = A[a]
        a += 1
    else:
        ret[idx] = B[b]
        b += 1
    idx += 1

while a < len(A):
    ret[idx] = A[a]
    a += 1
    idx += 1

while b < len(B):
    ret[idx] = B[b]
    b += 1
    idx += 1

print(" ".join(map(str, ret)))