import io
import sys

example = """
3 2
1 2 4
1 2 3
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


if __name__ == "__main__":
    input = sys.stdin.readline
    inf = float("inf")

    N, M = map(int, input().split())

    edges = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    dist = [inf] * (N + 1)
    dist[1] = 0

    for _ in range(N - 1):
        for u, v, w in edges:
            dist[v] = min(dist[v], dist[u] + w)

    is_cycle = False
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            is_cycle = True

    if is_cycle:
        print(-1)
    else:
        for v in range(2, N + 1):
            if dist[v] == inf:
                print(-1)
            else:
                print(dist[v])
