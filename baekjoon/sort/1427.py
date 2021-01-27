import io
import sys

example = """
2143
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline
print("".join(sorted(input(), reverse=True)))
