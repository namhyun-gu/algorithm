import io
import sys

example = """
4 2
1 1 1 1
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def solution(nums: list[int], m: int):
    ret, sum, s, e = 0, 0, 0, 0

    while True:
        if sum >= m:
            sum -= nums[s]
            s += 1
        elif e == len(nums):
            break
        else:
            sum += nums[e]
            e += 1
        if sum == m:
            ret += 1

    print(ret)


if __name__ == "__main__":
    input = sys.stdin.readline

    _, M = map(int, input().split())
    nums = [*map(int, input().split())]

    solution(nums, M)