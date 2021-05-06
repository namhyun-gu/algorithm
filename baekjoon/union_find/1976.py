# region Input redirection
import io
import sys

example = """
3
3
0 1 0
1 0 1
0 1 0
1 2 3
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def find(group, x):
    if group[x] == x:
        return x
    group[x] = find(group, group[x])
    return group[x]


def union(group, a, b):
    a = find(group, a)
    b = find(group, b)

    if a == b:
        return
    group[b] = a


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    M = int(input())

    group = [i for i in range(N)]
    graph = []

    for a in range(N):
        graph.append(list(map(int, input().split())))

        for b, conn in enumerate(graph[a]):
            if conn:
                union(group, a, b)

    plan = list(map(int, input().split()))

    is_able = True

    for i in range(M - 1):
        a = plan[i] - 1
        b = plan[i + 1] - 1

        if find(group, a) != find(group, b):
            is_able = False
            break

    if is_able:
        print("YES")
    else:
        print("NO")