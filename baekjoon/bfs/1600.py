import io
import sys

example = """
1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import collections

hourse_dir = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(board):
    visited = [[[0 for _ in range(W)] for _ in range(H)] for _ in range(K + 1)]

    queue = collections.deque([(0, 0, K)])
    while queue:
        r, c, k = queue.popleft()
        if r == H - 1 and c == W - 1:
            return visited[k][r][c]

        if k > 0:
            for dr, dc in hourse_dir:
                tr, tc = r + dr, c + dc
                if tr in range(H) and tc in range(W):
                    if not visited[k - 1][tr][tc] and board[tr][tc] == 0:
                        visited[k - 1][tr][tc] = visited[k][r][c] + 1
                        queue.append((tr, tc, k - 1))

        for dr, dc in dir:
            tr, tc = r + dr, c + dc
            if tr in range(H) and tc in range(W):
                if not visited[k][tr][tc] and board[tr][tc] == 0:
                    visited[k][tr][tc] = visited[k][r][c] + 1
                    queue.append((tr, tc, k))

    return -1


if __name__ == "__main__":
    input = sys.stdin.readline

    K = int(input())
    W, H = map(int, input().split())

    board = [[*map(int, input().split())] for _ in range(H)]

    print(bfs(board))