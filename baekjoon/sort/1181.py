from .. import util

example = """
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
"""
util.setinput(example)

import sys

input = sys.stdin.readline
N = int(input())
words = set()
for _ in range(N):
    word = input().rstrip()
    words.add((len(word), word))


for word in sorted(words):
    print(word[1])