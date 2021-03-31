import io
import sys

example = """
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
0
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import heapq


def neighbor(r, c, n):
    neighbor = []
    if r + 1 in range(n):
        neighbor.append((r + 1, c))
    if r - 1 in range(n):
        neighbor.append((r - 1, c))
    if c + 1 in range(n):
        neighbor.append((r, c + 1))
    if c - 1 in range(n):
        neighbor.append((r, c - 1))
    return neighbor


if __name__ == "__main__":
    input = sys.stdin.readline
    inf = float("inf")

    T = 0
    while True:
        T += 1
        N = int(input())
        if N == 0:
            break

        cave = []
        for _ in range(N):
            cave.append([*map(int, input().split())])

        cost = [[inf] * N for _ in range(N)]
        cost[0][0] = cave[0][0]

        heap = []
        heapq.heappush(heap, (cave[0][0], 0, 0))

        while heap:
            _, r, c = heapq.heappop(heap)

            for next in neighbor(r, c, N):
                next_r, next_c = next

                alt = cost[r][c] + cave[next_r][next_c]
                if alt < cost[next_r][next_c]:
                    cost[next_r][next_c] = alt
                    heapq.heappush(heap, (alt, next_r, next_c))

        print(f"Problem {T}: {cost[N - 1][N - 1]}")