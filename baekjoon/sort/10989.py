from .. import util

example = """
10
5
2
3
1
4
2
3
5
1
7
"""
util.setinput(example)

import sys

input = sys.stdin.readline

nums = dict()
N = int(input())

for _ in range(N):
    num = int(input())
    if num in nums:
        nums[num] += 1
    else:
        nums[num] = 1

sort_nums = sorted(nums.keys())
for num in sort_nums:
    for _ in range(nums[num]):
        print(num)