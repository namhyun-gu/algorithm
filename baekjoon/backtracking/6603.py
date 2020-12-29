import io
import sys

example = """
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
"""
sys.stdin = io.StringIO(example.strip())

import sys
import itertools

input = sys.stdin.readline

while True:
    k, *S = list(map(int, input().split()))
    if k == 0:
        break

    for nums in itertools.combinations(S, 6):
        print(" ".join(map(str, nums)))
    print()