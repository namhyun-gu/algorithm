from .. import util

example = """
5 17
"""
util.setinput(example)

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque([N])
dist = [-1 for _ in range(100001)]
way = [0 for _ in range(100001)]
dist[N] = 0
way[N] = 1

while queue:
    current = queue.popleft()

    if current == K:
        break

    for next in [current * 2, current - 1, current + 1]:
        if 0 <= next <= 100000:
            if dist[next] == -1:
                dist[next] = dist[current] + 1
                way[next] = way[current]
                queue.append(next)
            elif dist[next] == dist[current] + 1:
                # 이전에 방문했을 때의 거리가 다른 방법으로 방문하는 거리와 같은 경우
                way[next] += way[current]

print(dist[K])
print(way[K])
