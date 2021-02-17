import io
import sys

example = """
10 15
5 1 3 5 10 7 4 9 2 8
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def solution(nums, S):
    s, e, sum, length = 0, 0, 0, 0
    ret = len(nums) + 1

    while True:
        if sum >= S:
            sum -= nums[s]
            s += 1
            length -= 1
        elif e == len(nums):
            break
        else:
            sum += nums[e]
            e += 1
            length += 1

        if sum >= S:
            ret = min(ret, length)

    if ret == len(nums) + 1:
        print(0)
    else:
        print(ret)


if __name__ == "__main__":
    input = sys.stdin.readline

    N, S = map(int, input().split())
    nums = [*map(int, input().split())]

    solution(nums, S)