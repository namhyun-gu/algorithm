"""
0-1 BFS

BFS 탐색 시 가중치가 없는 경로는 큐에 추가할 때 큐의 맨 앞에 추가하여 탐색

Ref: https://justicehui.github.io/medium-algorithm/2018/08/30/01BFS/

관련 문제 : http://boj.kr/13549 (숨바꼭질 3)
"""
from collections import deque

N, K = 5, 17

queue = deque([N])
dist = [-1 for _ in range(100001)]
dist[N] = 0

while queue:
    current = queue.popleft()
    if current == K:
        break

    if current * 2 <= 100000 and dist[current * 2] == -1:
        dist[current * 2] = dist[current]
        # 비용이 없으므로 큐의 맨 앞에 추가
        queue.appendleft(current * 2)

    if current - 1 >= 0 and dist[current - 1] == -1:
        dist[current - 1] = dist[current] + 1
        queue.append(current - 1)

    if current + 1 <= 100000 and dist[current + 1] == -1:
        dist[current + 1] = dist[current] + 1
        queue.append(current + 1)

print(dist[K])
