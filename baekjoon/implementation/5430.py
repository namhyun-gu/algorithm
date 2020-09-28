from .. import util

example = """
5
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
R
0
[]
"""
util.setinput(example)

import sys
from collections import deque
input = sys.stdin.readline


def arr_to_str(arr):
    result = '['
    for idx in range(len(arr)):
        result += str(arr[idx])
        if idx != len(arr) - 1:
            result += ','
    result += ']'
    return result


T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    arr = input().strip()[1:-1]
    if len(arr) == 0:
        arr = []
    else:
        arr = deque(list(map(int, arr.split(','))))

    error = False
    reverse = False
    for c in p:
        if c == 'R':
            reverse = not reverse
        elif c == 'D':
            if len(arr) == 0:
                error = True
                break
            if reverse:
                arr.pop()
            else:
                arr.popleft()

    if error:
        print("error")
    else:
        if reverse:
            arr.reverse()
        print(arr_to_str(arr))
