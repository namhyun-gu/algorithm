from .. import util

example = """
5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
"""
util.setinput(example)

import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())
city = [[0 for _ in range(N)] for _ in range(N)]
house = []
chicken = []

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        cur = line[j]
        if cur == 1:
            house.append((i, j))
        if cur == 2:
            chicken.append((i, j))
        city[i][j] = cur

min_dist = 1e4
for picks in itertools.combinations(chicken, M):
    dists = [1e4] * len(house)
    for idx in range(len(house)):
        for cx, cy in picks:
            hx, hy = house[idx]
            dists[idx] = min(dists[idx], abs(hx - cx) + abs(hy - cy))
    min_dist = min(min_dist, sum(dists))
print(min_dist)
