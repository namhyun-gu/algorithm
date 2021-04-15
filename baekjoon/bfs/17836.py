import io
import sys

example = """
6 6 16
0 0 0 0 1 1
0 0 0 0 0 2
1 1 1 0 1 0
0 0 0 0 0 0
0 1 1 1 1 1
0 0 0 0 0 0
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import collections


def bfs():
    queue = collections.deque()
    queue.append((0, 0, 0, False))

    visit = [[[0, 0] for _ in range(M)] for _ in range(N)]
    visit[0][0][False] = 0

    while queue:
        cr, cc, cnt, can_break = queue.popleft()

        if castle[cr][cc] == 2:
            can_break = True

        if cr == N - 1 and cc == M - 1:
            return cnt

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = cr + dr, cc + dc

            if nr not in range(N) or nc not in range(M):
                continue

            if visit[nr][nc][can_break]:
                continue

            if can_break:
                visit[nr][nc][can_break] = 1
                queue.append((nr, nc, cnt + 1, can_break))
            else:
                if castle[nr][nc] != 1:
                    visit[nr][nc][can_break] = 1
                    queue.append((nr, nc, cnt + 1, can_break))
    return -1


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M, T = map(int, input().split())

    castle = [[*map(int, input().split())] for _ in range(N)]

    sword = None
    for n in range(N):
        for m in range(M):
            if castle[n][m] == 2:
                sword = (m, n)

    min_time = bfs()
    if 0 < min_time <= T:
        print(min_time)
    else:
        print("Fail")
