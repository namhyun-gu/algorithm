# region Input redirection
import io
import sys

example = """
3
2 1 4
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import itertools

if __name__ == "__main__":
    input = sys.stdin.readline

    _ = int(input())
    nums = list(map(int, input().split()))

    max_num = sum(nums)
    slot = [0 for _ in range(max_num + 1)]
    slot[max_num] = 1

    for num in nums:
        slot[num] = 1

    for n in range(2, len(nums)):
        for pick in itertools.combinations(nums, n):
            slot[sum(pick)] = 1

    for i in range(1, max_num):
        if not slot[i]:
            print(i)
            exit(0)

    print(max_num + 1)