# region Input redirection
import io
import sys

example = """
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
from collections import deque


def fill(board, r, c):
    queue = deque()
    queue.append((r, c))

    dist = [[0 for _ in range(C)] for _ in range(R)]
    dist[r][c] = 1

    while queue:
        r, c = queue.popleft()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc

            if nr not in range(R) or nc not in range(C):
                continue

            if board[nr][nc] != "L":
                continue

            if not dist[nr][nc]:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    return dist[r][c] - 1


if __name__ == "__main__":
    input = sys.stdin.readline

    R, C = map(int, input().split())

    board = [[*input().rstrip()] for _ in range(R)]

    answer = 0

    for r in range(R):
        for c in range(C):
            if board[r][c] == "L":
                answer = max(answer, fill(board, r, c))

    print(answer)