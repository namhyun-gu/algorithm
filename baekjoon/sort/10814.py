from .. import util

example = """
3
21 Junkyu
21 Dohyun
20 Sunyoung
"""
util.setinput(example)

import sys

input = sys.stdin.readline

N = int(input())
members = []

for n in range(N):
    age, name = input().rstrip().split()
    members.append((int(age), n, name))

for member in sorted(members):
    age, _, name = member
    print(age, name)