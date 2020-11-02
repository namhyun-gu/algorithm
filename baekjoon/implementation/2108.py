from .. import util

example = """
5
-1
-2
-3
-1
-2
"""
util.setinput(example)

import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
nums = sorted([int(input()) for _ in range(N)])

count = Counter(nums).most_common()

# 정수 나눗셈으로 나누게 되면 값을 버리기 때문에, round를 통해 올려줘야한다.
print(round(sum(nums) / N))
print(nums[N // 2])
if len(nums) > 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])
print(nums[-1] - nums[0])
