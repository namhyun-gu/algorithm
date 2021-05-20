# region Input redirection
import io
import sys

example = """
8 19
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 0
0 0 1 0 1 0 0 1 1 0 0 1 0 0 0 1 0 0 0
0 1 0 0 0 1 0 1 0 1 0 1 0 0 0 1 0 0 0
0 1 1 1 1 1 0 1 0 1 0 1 0 0 0 1 0 0 0
0 1 0 0 0 1 0 1 0 0 1 1 0 0 0 1 0 0 0
0 1 0 0 0 1 0 1 0 0 0 1 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys

sys.setrecursionlimit(10 ** 9)

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def dfs(board, r, c):
    board[r][c] = 0

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc

        if nr not in range(R) or nc not in range(C):
            continue

        if not board[nr][nc]:
            continue

        dfs(board, nr, nc)


if __name__ == "__main__":
    input = sys.stdin.readline

    R, C = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(R)]
    answer = 0

    for r in range(R):
        for c in range(C):
            if not board[r][c]:
                continue

            answer += 1
            dfs(board, r, c)

    print(answer)