from .. import util

example = """
0 4 2 5 6
"""
util.setinput(example)

import sys
input = sys.stdin.readline

nums = map(int, input().split())
acc = 0
for num in nums:
    acc += pow(num, 2)
print(acc % 10)
