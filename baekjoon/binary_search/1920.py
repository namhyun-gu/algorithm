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
A = list(sorted(map(int, input().split())))
_ = int(input())
nums = list(map(int, input().split()))


def search(arr, value, left, right):
    if left > right:
        return 0

    mid = (left + right) // 2
    if arr[mid] > value:
        return search(arr, value, left, mid - 1)
    elif arr[mid] < value:
        return search(arr, value, mid + 1, right)
    return 1


for num in nums:
    print(search(A, num, 0, len(A) - 1))