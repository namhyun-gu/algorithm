from .. import util

example = """
5
4 1 5 2 3
5
1 3 7 9 5
"""
util.setinput(example)

import sys

input = sys.stdin.readline
_ = int(input())
A = list(map(int, input().split()))

a_dict = dict()
for num in A:
    a_dict[num] = 1

_ = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num in a_dict:
        print(1)
    else:
        print(0)