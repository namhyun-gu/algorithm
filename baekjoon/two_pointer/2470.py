import io
import sys

example = """
5
-2 4 -99 -1 98
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys

input = sys.stdin.readline

_ = input()
water = sorted(map(int, input().split()))

s, e = 0, len(water) - 1
ret = water[s], water[e]
minimum = abs(water[s] + water[e])

while s < e:
    mix = water[s] + water[e]

    if abs(mix) < minimum:
        minimum = abs(mix)
        ret = water[s], water[e]

    if mix < 0:
        s += 1
    else:
        e -= 1

print(ret[0], ret[1])