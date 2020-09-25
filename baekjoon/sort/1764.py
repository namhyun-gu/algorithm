from .. import util

example = """
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
"""
util.setinput(example)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

no_hear = set()
no_see = set()

for _ in range(N):
    no_hear.add(input().strip())

for _ in range(M):
    no_see.add(input().strip())

no_hear_see = no_hear.intersection(no_see)

print(len(no_hear_see))
sorted_no_hear_see = sorted(no_hear_see)

for item in sorted_no_hear_see:
    print(item)
