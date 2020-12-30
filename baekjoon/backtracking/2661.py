import io
import sys

example = """
7
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

N = int(input())


def is_good(picks):
    window = 2
    while window <= len(picks) // 2:
        a = picks[-window:]
        b = picks[-window * 2 : -window]

        if a == b:
            return False
        window += 1
    return True


def permutations(picks, r):
    if len(picks) == r:
        print("".join(map(str, picks)))
        exit(0)

    for num in [1, 2, 3]:
        if not picks or num != picks[-1]:
            next = [*picks, num]
            if len(next) < 4 or is_good(next):
                permutations(next, r)


permutations([], N)