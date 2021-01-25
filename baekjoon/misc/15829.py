import io
import sys

example = """
5
abcde
"""
sys.stdin = io.StringIO(example.strip())

import sys
from functools import reduce

input = sys.stdin.readline

L = int(input())
string = input().strip()

r = 31
M = 1234567891

ret = (
    reduce(
        lambda acc, it: acc + (it[0] * pow(r, it[1])),
        zip(map(lambda it: ord(it) - 96, string), range(0, L)),
        0,
    )
    % M
)

print(ret)