import io
import sys

example = """
1
3
Fred Barney
Betty Wilma
Barney Betty
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def find(network, x):
    if network[x] == x:
        return x
    network[x] = find(network, network[x])
    return network[x]


def union(network, count, x, y):
    x_root = find(network, x)
    y_root = find(network, y)

    if x_root == y_root:
        return
    network[y_root] = x_root
    count[x_root] += count[y_root]


if __name__ == "__main__":
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        F = int(input())

        network = {}
        count = {}
        for _ in range(F):
            A, B = input().split()

            if A not in network:
                network[A] = A
                count[A] = 1
            if B not in network:
                network[B] = B
                count[B] = 1

            union(network, count, A, B)
            print(count[find(network, A)])
