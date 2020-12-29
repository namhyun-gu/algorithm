import io
import sys

example = """
5 0
-7 -3 -2 5 8
"""
sys.stdin = io.StringIO(example.strip())

import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
for r in range(1, N + 1):
    for picks in combinations(nums, r):
        if sum(picks) == S:
            cnt += 1

print(cnt)