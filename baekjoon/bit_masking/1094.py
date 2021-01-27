import io
import sys

example = """
48
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

X = int(input())
print(bin(X).count("1"))
