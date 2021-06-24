# region Input redirection
import io
import sys

example = """
10 10 8
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import heapq


def get_archer_cases():
    for a in range(M):
        for b in range(a + 1, M):
            for c in range(b + 1, M):
                yield (a, b, c)


def simulation(board, archer_case):
    removed = 0
    while calculate_enemy(board) > 0:
        removed += attack(board, archer_case)
        move_enemy(board)
    return removed


def calculate_enemy(board):
    enemy = 0
    for n in range(N):
        for m in range(M):
            if board[n][m] == 1:
                enemy += 1
    return enemy


def distance(ar, ac, br, bc):
    return abs(ar - br) + abs(ac - bc)


def attack(board, archer_case):
    attacked = [[0 for _ in range(M)] for _ in range(N)]
    attack_list = []

    for archer in archer_case:
        heap = []
        for i in range(N - 1, -1, -1):
            for j in range(M):
                if board[i][j] == 1:
                    dist = distance(N, archer, i, j)
                    if dist <= D:
                        heapq.heappush(heap, (dist, j, i))
        if heap:
            _, c, r = heapq.heappop(heap)
            attack_list.append((r, c))

    count = 0
    for r, c in attack_list:
        if not attacked[r][c]:
            attacked[r][c] = True
            count += 1
            board[r][c] = 0
    return count


def move_enemy(board):
    for n in range(N - 1, -1, -1):
        for m in range(M):
            if board[n][m] == 1:
                board[n][m] = 0
                next = n + 1
                if next == N:
                    continue
                board[next][m] = 1


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M, D = map(int, input().split())

    board = [[*map(int, input().split())] for _ in range(N)]

    answer = 0
    for archer_case in get_archer_cases():
        board_copy = [[board[i][j] for j in range(M)] for i in range(N)]
        answer = max(answer, simulation(board_copy, archer_case))

    print(answer)