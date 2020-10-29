from .. import util

example = """
6 8 10
25 52 60
5 12 13
0 0 0
"""
util.setinput(example)

import sys
input = sys.stdin.readline

def is_triangle(a, b, c):
    a = pow(a, 2)
    b = pow(b, 2)
    c = pow(c, 2)

    return a == b + c or b == a + c or c == a + b


while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break
    else:
        a, b, c = line
        if is_triangle(a, b, c):
            print("right")
        else:
            print("wrong")