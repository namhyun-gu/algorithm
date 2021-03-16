import io
import sys

example = """
5 4
3 1
3 2
4 3
5 3
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
from collections import deque


def bfs(graph, start):
    queue = deque([start])
    visit = [0 for _ in range(len(graph))]
    visit[start] = 1
    count = 0

    while queue:
        cur = queue.popleft()
        count += 1

        for trust in graph[cur]:
            if not visit[trust]:
                queue.append(trust)
                visit[trust] = 1

    return count


def solution(graph, n):
    ret = []
    max_count = 0
    for i in range(1, n + 1):
        if graph[i]:
            count = bfs(graph, i)
            if count >= max_count:
                if count > max_count:
                    ret = []
                max_count = count
                ret.append(i)

    print(*ret)


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[b].append(a)

    solution(graph, N)