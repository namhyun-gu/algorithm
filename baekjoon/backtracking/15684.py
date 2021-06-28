# region Input redirection
import io
import sys

example = """
10 5 30
30 9
3 2
2 3
5 1
5 4
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def simulate():
    for line in range(N):
        cur = line

        for h in range(H):
            if board[h][cur]:
                cur += 1
            elif board[h][cur - 1]:
                cur -= 1

        if cur != line:
            return False

    return True


def dfs(index, r, depth=0):
    global answer

    if r == depth:
        if simulate():
            answer = r
        return

    for h in range(index, H):
        for line in range(N - 1):
            if board[h][line]:
                continue

            if line - 1 >= 0 and board[h][line - 1]:
                continue

            if line + 1 < N and board[h][line + 1]:
                continue

            board[h][line] = 1
            dfs(h, r, depth + 1)
            board[h][line] = 0


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M, H = map(int, input().split())
    board = [[0] * N for _ in range(H)]

    for _ in range(M):
        a, b = map(int, input().split())
        board[a - 1][b - 1] = 1  # a번 위치에 b에서 b + 1로 가는 가로선

    answer = -1
    for r in range(4):
        dfs(0, r)

        if answer != -1:
            break

    print(answer)
