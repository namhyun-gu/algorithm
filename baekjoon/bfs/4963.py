# region Input redirection
import io
import sys

example = """
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
from collections import deque


def can_walk(board, visit, w, h):
    H = len(board)
    W = len(board[0])

    if w not in range(W) or h not in range(H):
        return False

    return board[h][w] == 1 and not visit[h][w]


def bfs(board, visit, w, h):
    queue = deque()
    queue.append((w, h))

    while queue:
        cw, ch = queue.popleft()

        for th in [-1, 0, 1]:
            for tw in [-1, 0, 1]:
                if th == 0 and tw == 0:
                    continue

                nw = cw + tw
                nh = ch + th

                if can_walk(board, visit, nw, nh):
                    visit[nh][nw] = 1
                    queue.append((nw, nh))


if __name__ == "__main__":
    input = sys.stdin.readline

    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break

        visit = [[0] * W for _ in range(H)]
        board = [[*map(int, input().split())] for _ in range(H)]

        cnt = 0

        for h in range(H):
            for w in range(W):
                if can_walk(board, visit, w, h):
                    visit[h][w] = 1
                    bfs(board, visit, w, h)
                    cnt += 1

        print(cnt)