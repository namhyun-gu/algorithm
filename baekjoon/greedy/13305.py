import io
import sys

example = """
4
2 3 1
5 2 4 1
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

N = int(input())
dists = [*map(int, input().split())]
prices = [*map(int, input().split())]

ret = 0
min_price = prices[0]

for i in range(N - 1):
    min_price = min(min_price, prices[i])
    ret += min_price * dists[i]

print(ret)