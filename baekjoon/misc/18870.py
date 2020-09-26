from .. import util

example = """
6
1000 999 1000 999 1000 999
"""
util.setinput(example)

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

map = {}
sorted_nums = sorted(set(nums))
for idx in range(len(sorted_nums)):
    map[sorted_nums[idx]] = idx

for num in nums:
    print(map[num], end=" ")
