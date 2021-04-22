import io
import sys

example = """
5 2 6
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def spring_and_summer():
    for r in range(N):
        for c in range(N):
            if not tree[r][c]:
                continue

            tree[r][c].sort()

            for idx, t in enumerate(tree[r][c]):
                if t <= ground[r][c]:
                    ground[r][c] -= t
                    tree[r][c][idx] += 1
                else:
                    die = tree[r][c][idx:]
                    for d in die:
                        ground[r][c] += d // 2
                    tree[r][c] = tree[r][c][:idx]
                    break


def dir(r, c):
    return [
        (r - 1, c - 1),
        (r - 1, c),
        (r - 1, c + 1),
        (r, c - 1),
        (r, c + 1),
        (r + 1, c - 1),
        (r + 1, c),
        (r + 1, c + 1),
    ]


def fall():
    for r in range(N):
        for c in range(N):
            if tree[r][c]:
                cnt = 0
                for t in tree[r][c]:
                    if t % 5 == 0:
                        cnt += 1

                if cnt:
                    for _ in range(cnt):
                        for tr, tc in dir(r, c):
                            if tr in range(N) and tc in range(N):
                                tree[tr][tc].append(1)


def winter():
    for r in range(N):
        for c in range(N):
            ground[r][c] += append[r][c]


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M, K = map(int, input().split())

    ground = [[5] * N for _ in range(N)]
    tree = [[[] for _ in range(N)] for _ in range(N)]
    append = [list(map(int, input().split())) for _ in range(N)]

    for _ in range(M):
        x, y, z = map(int, input().split())
        tree[x - 1][y - 1].append(z)

    for _ in range(K):
        spring_and_summer()
        fall()
        winter()

    ans = 0
    for r in range(N):
        for c in range(N):
            ans += len(tree[r][c])

    print(ans)