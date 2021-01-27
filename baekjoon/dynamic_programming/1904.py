import io
import sys

example = """
4
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

N = int(input())

if N == 1 or N == 2:
    print(N)
else:
    a, b = 1, 2
    for n in range(3, N + 1):
        a, b = b, (a + b) % 15746
    print(b % 15746)