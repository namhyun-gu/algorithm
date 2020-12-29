import io
import sys

example = """
10
1 4 2 3 1 4 2 3 1 2
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline
N = int(input())
print(" ".join(map(str, sorted(set(map(int, input().split()))))))