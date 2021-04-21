import io
import sys

example = """
6 6
001111
010000
001111
110001
011010
100010
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import collections


def bfs():
    queue = collections.deque()
    queue.append((0, 0, 0))

    visit = [[0 for _ in range(M)] for _ in range(N)]
    visit[0][0] = 1

    while queue:
        r, c, broken = queue.popleft()

        if r == N - 1 and c == M - 1:
            return broken

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            tr, tc = r + dr, c + dc
            if tr in range(N) and tc in range(M):
                if not visit[tr][tc]:
                    visit[tr][tc] = 1
                    if board[tr][tc] == "1":
                        queue.append((tr, tc, broken + 1))
                    else:
                        queue.appendleft((tr, tc, broken))

    return 0


if __name__ == "__main__":
    input = sys.stdin.readline

    M, N = map(int, input().split())

    board = [input() for _ in range(N)]

    print(bfs())