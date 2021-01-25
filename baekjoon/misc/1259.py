import io
import sys

example = """
121
1231
12421
0
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

while True:
    line = input().strip()
    if int(line) == 0:
        break

    if line == line[::-1]:
        print("yes")
    else:
        print("no")
