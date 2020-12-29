import io
import sys

example = """
2
4 2
"""
sys.stdin = io.StringIO(example.strip())

import sys
from functools import reduce

input = sys.stdin.readline

_ = input()
nums = list(map(int, input().split()))

a, b = min(nums), max(nums)
print(a * b)