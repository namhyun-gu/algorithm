import io
import sys

example = """
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import heapq


def find(x):
    if group[x] < 0:
        return x
    group[x] = find(group[x])
    return group[x]


def union(u, v):
    u = find(u)
    v = find(v)
    if u == v:
        return False
    if group[u] == group[v]:
        group[u] -= 1
    if group[u] < group[v]:
        group[v] = u
    else:
        group[u] = v
    return True


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    group = [-1] * (N + 1)
    edges = []

    for _ in range(M):
        s, e, w = map(int, input().split())
        heapq.heappush(edges, (w, s, e))

    cnt = 0
    cost = 0
    # MST는 N - 1개의 길을 연결, N - 2개 길만 연결하여 두 개의 마을로 나눔
    while cnt < N - 2:
        w, s, e = heapq.heappop(edges)
        if find(s) != find(e):
            cost += w
            cnt += 1
            union(s, e)

    print(cost)