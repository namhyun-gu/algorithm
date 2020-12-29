import io
import sys

example = """
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
"""
sys.stdin = io.StringIO(example.strip())

import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
cards = sorted(map(int, input().split()))
count = Counter(cards)
M = input()


def search(num):
    l, r = 0, N - 1

    while l <= r:
        mid = (l + r) // 2

        if num == cards[mid]:
            return True
        elif num < cards[mid]:
            r = mid - 1
        elif num > cards[mid]:
            l = mid + 1
    return False


ret = []
for num in map(int, input().split()):
    ret.append(count[num] if search(num) else 0)
print(" ".join(map(str, ret)))