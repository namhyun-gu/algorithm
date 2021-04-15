import io
import sys

example = """
4 4
0100
0111
1111
0111
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())

    board = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for n in range(1, N + 1):
        line = input()
        for m in range(1, M + 1):
            board[n][m] = int(line[m - 1])

    size = 0

    for n in range(1, N + 1):
        for m in range(1, M + 1):
            if board[n][m] == 1:
                board[n][m] = (
                    min(board[n - 1][m], board[n][m - 1], board[n - 1][m - 1]) + 1
                )
                size = max(size, board[n][m])
    print(size * size)