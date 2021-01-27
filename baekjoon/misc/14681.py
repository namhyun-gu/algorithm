import io
import sys

example = """
12
5
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

X = int(input())
Y = int(input())

if X > 0 and Y > 0:
    print(1)
elif X < 0 and Y > 0:
    print(2)
elif X > 0 and Y < 0:
    print(4)
elif X < 0 and Y < 0:
    print(3)