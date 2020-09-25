from .. import util

example = """
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1
"""
util.setinput(example)

import sys
input = sys.stdin.readline


def to_bits(idx):
    return 1 << int(idx) - 1


S = 0
M = int(input())
for _ in range(M):
    line = input().split()
    if len(line) > 1:
        operation, param = line
        if operation == "add":
            S = S | to_bits(param)
        elif operation == "check":
            check = S & to_bits(param)
            if check > 0:
                print(1)
            else:
                print(0)
        elif operation == "toggle":
            S = S ^ to_bits(param)
        elif operation == "remove":
            S = S & ~(to_bits(param))
    else:
        operation = line[0]
        if operation == "empty":
            S = 0
        elif operation == "all":
            S = S | int('0xFFFFF', 16)
