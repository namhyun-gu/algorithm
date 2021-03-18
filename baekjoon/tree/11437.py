import io
import sys

example = """
15
1 2
1 3
2 4
3 7
6 2
3 8
4 9
2 5
5 11
7 13
10 4
11 15
12 5
14 7
6
6 11
10 9
2 6
7 6
8 13
8 15
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import collections


def lca(depth, parent, a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    while depth[a] != depth[b]:
        b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]
    return a


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    tree = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        a, b = map(int, input().rstrip().split())
        tree[a].append(b)
        tree[b].append(a)

    queue = collections.deque([1])
    depth = [0 for _ in range(N + 1)]
    parent = [0 for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    visited[1] = True

    while queue:
        current = queue.popleft()

        for next in tree[current]:
            if not visited[next]:
                visited[next] = True
                depth[next] = depth[current] + 1
                parent[next] = current
                queue.append(next)

    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        print(lca(depth, parent, a, b))