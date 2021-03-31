import io
import sys

example = """
2 0 1 2
0 1 1000
1 1 10
11 11
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import collections

if __name__ == "__main__":
    input = sys.stdin.readline
    inf = float("inf")

    N, S, E, M = map(int, input().split())

    edges = []
    graph = [[] for _ in range(N)]
    for _ in range(M):
        s, e, price = map(int, input().split())
        edges.append((s, e, price))
        graph[s].append((e, price))

    benefit = [*map(int, input().split())]

    prices = [inf] * N
    prices[S] = -benefit[S]

    for _ in range(N - 1):
        for s, e, price in edges:
            if prices[s] + price - benefit[e] < prices[e]:
                prices[e] = prices[s] + price - benefit[e]

    visit = [0] * N
    cycles = []
    for s, e, price in edges:
        if prices[s] + price - benefit[e] < prices[e]:
            visit[s] = True
            cycles.append(s)

    queue = collections.deque(cycles)
    while queue:
        s = queue.popleft()
        for e, price in graph[s]:
            if not visit[e]:
                visit[e] = True
                queue.append(e)

    if visit[E]:
        print("Gee")
    elif prices[E] == inf:
        print("gg")
    else:
        print(-prices[E])