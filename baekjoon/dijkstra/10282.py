import io
import sys

example = """
2
3 2 2
2 1 5
3 2 5
3 3 1
2 1 2
3 1 8
3 2 4
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import heapq

if __name__ == "__main__":
    input = sys.stdin.readline
    inf = sys.maxsize

    T = int(input())
    for _ in range(T):
        n, d, c = map(int, input().split())

        graph = [[] for _ in range(n + 1)]

        for _ in range(d):
            a, b, s = map(int, input().split())
            graph[b].append((a, s))

        dist = [inf] * (n + 1)
        dist[c] = 0

        heap = []
        heapq.heappush(heap, (0, c))

        while heap:
            _, u = heapq.heappop(heap)
            for v, w in graph[u]:
                alt = dist[u] + w
                if alt < dist[v]:
                    dist[v] = alt
                    heapq.heappush(heap, (alt, v))

        cnt = 0
        time = 0
        for v in range(1, n + 1):
            if dist[v] != inf:
                cnt += 1
                time = max(time, dist[v])

        print(cnt, time)