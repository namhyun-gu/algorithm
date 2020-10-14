from .. import util

example = """
5
1 3 5 7 1000
"""
util.setinput(example)

"""
에라토스테네스의 체

https://ko.wikipedia.org/wiki/에라토스테네스의_체
"""
import sys

input = sys.stdin.readline

MAX = 1000
sieve = [1 for _ in range(MAX + 1)]
sieve[0] = sieve[1] = 0

m = int(MAX ** 0.5)
for i in range(2, m + 1):
    if sieve[i]:
        for j in range(i + i, MAX + 1, i):
            sieve[j] = 0

_ = input()
cnt = 0
for num in map(int, input().split()):
    if sieve[num]:
        cnt += 1

print(cnt)
