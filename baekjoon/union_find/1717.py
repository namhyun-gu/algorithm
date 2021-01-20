import io
import sys

example = """
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""
sys.stdin = io.StringIO(example.strip())

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())

set = list(range(N + 1))


def get_parent(x):
    if x == set[x]:
        return x
    set[x] = get_parent(set[x])
    return set[x]


def union(a, b):
    a_parent = get_parent(a)
    b_parent = get_parent(b)

    if a_parent == b_parent:
        return

    set[b_parent] = a_parent


for _ in range(M):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    elif op == 1:
        if get_parent(a) == get_parent(b):
            print("YES")
        else:
            print("NO")