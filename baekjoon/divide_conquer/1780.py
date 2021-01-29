import io
import sys

example = """
9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

N = int(input())

paper = [[*map(int, input().split())] for _ in range(N)]

ret = [0, 0, 0]


def is_same(s_r, s_c, size):
    first = paper[s_c][s_r]
    for c in range(s_c, s_c + size):
        for r in range(s_r, s_r + size):
            if paper[c][r] != first:
                return first, False
    return first, True


def divide(r, c, size):
    num, is_valid = is_same(r, c, size)
    if is_valid:
        ret[num + 1] += 1
    else:
        d = size // 3
        if d >= 1:
            for n_c in [c, c + d, c + (d * 2)]:
                for n_r in [r, r + d, r + (d * 2)]:
                    divide(n_r, n_c, d)


divide(0, 0, N)

for cnt in ret:
    print(cnt)