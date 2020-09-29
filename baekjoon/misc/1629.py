from .. import util

example = """
2147483646 2147483647 2147483647
"""
util.setinput(example)

# Ref: https://mygumi.tistory.com/319
# Ref (2): https://www.acmicpc.net/board/view/48352
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())


def pow(a, b, c):
    if b == 0:
        return 1

    if b % 2 == 0:
        temp = pow(a, b / 2, c)
        return (temp * temp) % c
    else:
        temp = pow(a, (b - 1) / 2, c)
        return ((temp * temp) % c * a) % c


print(pow(A, B, C))
