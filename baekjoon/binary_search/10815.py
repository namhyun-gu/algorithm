import io
import sys

example = """
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int, input().strip().split())))

M = int(input())


def search(num):
    l, r = 0, N - 1

    while l <= r:
        mid = (l + r) // 2

        if cards[mid] == num:
            return True
        elif cards[mid] < num:
            l = mid + 1
        elif cards[mid] > num:
            r = mid - 1
    return False


ret = []
for num in map(int, input().strip().split()):
    ret.append("1" if search(num) else "0")

print(" ".join(ret))