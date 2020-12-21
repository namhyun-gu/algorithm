import io
import sys

example = """
3
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8
3
1 1 1
"""
sys.stdin = io.StringIO(example.strip())

import sys

sys.setrecursionlimit(111111)

input = sys.stdin.readline

T = int(input())


def dfs(cur, start):
    global group

    if group[cur]:
        if group[cur] != start:
            return 0
        else:
            n = 1
            temp = picks[cur]

            while temp != cur:
                n += 1
                group[temp] = start
                temp = picks[temp]
            return n
    else:
        group[cur] = start
        next = picks[cur]
        return dfs(next, start)


for _ in range(T):
    N = int(input())
    picks = [0] * (N + 1)
    group = [0] * (N + 1)

    for i, n in enumerate(map(int, input().split())):
        picks[i + 1] = n

    members = 0
    for n in range(1, N + 1):
        members += dfs(n, n)

    print(N - members)