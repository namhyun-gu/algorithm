from .. import util

example = """
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
"""
util.setinput(example)

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    wears = dict()
    for _ in range(N):
        name, category = input().strip().split()
        if category in wears:
            wears[category].append(name)
        else:
            wears[category] = [name]
    answer = 1
    for key in wears.keys():
        answer *= len(wears[key]) + 1
    print(answer - 1)
