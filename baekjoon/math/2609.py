from .. import util

example = """
24 18
"""
util.setinput(example)

"""
- 유클리드 호제법

https://ko.wikipedia.org/wiki/유클리드_호제법

a와 b의 최대공약수가 (a, b)이고,
a를 b로 나눈 나머지가 r일때
(a, b) = (b, r)

- 최소공배수

lcm(a, b) = a * b / gcd(a, b)
"""
import sys

input = sys.stdin.readline

a, b = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


g = gcd(a, b)
l = a * b // g

print(g, l)