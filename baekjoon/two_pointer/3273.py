import io
import sys

example = """
2
1 2
13
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def solution(nums: list[int], x: int):
    nums = sorted(nums)
    ret, s, e = 0, 0, len(nums) - 1

    while s < e:
        sum = nums[s] + nums[e]
        if sum <= x:
            s += 1
        else:
            e -= 1
        if sum == x:
            ret += 1
    print(ret)


if __name__ == "__main__":
    input = sys.stdin.readline

    _ = input()
    nums = [*map(int, input().split())]
    x = int(input())

    solution(nums, x)