import io
import sys

example = """
5
1 1 1 6 0
2 7 8 3 1
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().rstrip().split()))
B = sorted(map(int, input().rstrip().split()), reverse=True)

print(sum(map(lambda a, b: a * b, A, B)))