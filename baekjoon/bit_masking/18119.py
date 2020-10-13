from .. import util

example = """
5 10
apple
actual
banana
brick
courts
1 l
1 b
1 c
1 n
2 l
2 b
1 s
2 c
2 s
2 n
"""
util.setinput(example)

"""
다른 솔루션을 찾아보더라도 같은 방식으로 풀었는데
python이 시간초과되어 pypy3로 제출하더라도 시간초과됨
C++로 작성하여 해결
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
words = []
for n in range(N):
    word = input().rstrip()
    word_bit = 0
    for c in word:
        word_bit = word_bit | 1 << ord(c) - 97
    words.append(word_bit)

remember = 0x3ffffff


for _ in range(M):
    op, ch = input().split()
    if op == "1":
        remember = remember & ~(1 << ord(ch) - 97)
    else:
        remember = remember | (1 << ord(ch) - 97)

    cnt = 0
    for word in words:
        if word == remember & word:
            cnt += 1
    print(cnt)
