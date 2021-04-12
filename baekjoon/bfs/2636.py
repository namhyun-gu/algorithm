import io
import sys

example = """
5 5 
0 0 0 0 0 
0 1 1 0 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import collections


def bfs():
    queue = collections.deque()
    queue.append((0, 0))
    visit = set()

    while queue:
        r, c = queue.popleft()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            tr, tc = r + dr, c + dc

            if (tr, tc) not in visit and tr in range(R) and tc in range(C):
                visit.add((tr, tc))
                if board[tr][tc] == 0:
                    queue.append((tr, tc))
                else:
                    board[tr][tc] = "c"


def melt():
    remain = 0
    for r in range(R):
        for c in range(C):
            if board[r][c] == "c":
                board[r][c] = 0
            elif board[r][c] == 1:
                remain += 1
    return remain


if __name__ == "__main__":
    input = sys.stdin.readline

    R, C = map(int, input().split())

    board = [[*map(int, input().split())] for _ in range(R)]
    last_remain = 0

    for r in range(R):
        for c in range(C):
            if board[r][c] == 1:
                last_remain += 1

    cnt = 0
    while True:
        cnt += 1
        bfs()
        remain = melt()
        if remain == 0:
            break
        else:
            last_remain = remain

    print(cnt)
    print(last_remain)
