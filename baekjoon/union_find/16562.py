# region Input redirection
import io
import sys

example = """
5 3 10
10 10 20 20 30
1 3
2 4
5 4
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def find(friends, x):
    if friends[x] == x:
        return x

    friends[x] = find(friends, friends[x])
    return friends[x]


def union(friends, a, b):
    a = find(friends, a)
    b = find(friends, b)

    if a == b:
        return

    if prices[a] < prices[b]:
        friends[b] = a
    else:
        friends[a] = b


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M, k = map(int, input().split())

    prices = [0, *map(int, input().split())]

    friends = [i for i in range(N + 1)]

    for _ in range(M):
        v, w = map(int, input().split())
        union(friends, v, w)

    cost = 0
    for b in range(1, N + 1):
        if friends[b] == b:
            cost += prices[b]

    if cost <= k:
        print(cost)
    else:
        print("Oh no")