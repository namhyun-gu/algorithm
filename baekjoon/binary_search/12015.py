import io
import sys

example = """
3
10 30 20
"""
sys.stdin = io.StringIO(example.strip())

import sys
import bisect

input = sys.stdin.readline

_ = int(input())
nums = [*map(int, input().split())]
lis = [nums[0]]

for i in range(1, len(nums)):
    num = nums[i]
    if num > lis[-1]:
        lis.append(num)
    else:
        idx = bisect.bisect_left(lis, num)
        lis[idx] = num

print(len(lis))