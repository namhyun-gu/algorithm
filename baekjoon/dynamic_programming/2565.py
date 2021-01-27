import io
import sys

example = """
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

N = int(input())

lines = []

for _ in range(N):
    a, b = map(int, input().split())
    lines.append((a, b))

lines.sort()


def lis(sequence):
    ret = 0
    memo = [0] * len(sequence)
    for i in range(len(sequence)):
        memo[i] = 1
        for j in range(0, i):
            if sequence[i] > sequence[j]:
                memo[i] = max(memo[i], memo[j] + 1)
        ret = max(ret, memo[i])
    return ret


len = lis(list(map(lambda it: it[1], lines)))
print(N - len)