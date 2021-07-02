# region Input redirection
import io
import sys

example = """
2 6
7
10
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def possible(T, M, mid):
    return sum(mid // t for t in T) >= M


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    T = [int(input()) for _ in range(N)]

    lo, hi = 1, max(T) * M
    answer = sys.maxsize

    while lo <= hi:
        mid = (lo + hi) // 2

        if possible(T, M, mid):
            answer = min(answer, mid)
            hi = mid - 1
        else:
            lo = mid + 1

    print(answer)