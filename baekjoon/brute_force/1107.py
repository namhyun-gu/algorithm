import io
import sys

example = """
5457
3
6 7 8
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def button_count(n, broken):
    if n == 0:
        if broken[0]:
            return 0
        else:
            return 1
    cnt = 0
    while n > 0:
        if broken[n % 10]:
            return 0
        n //= 10
        cnt += 1
    return cnt


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    M = int(input())

    broken = [0 for _ in range(10)]

    for b in map(int, input().split()):
        broken[b] = 1

    min_cnt = abs(N - 100)

    for n in range(1000000):
        button = button_count(n, broken)
        if button > 0:
            press = abs(N - n)
            min_cnt = min(min_cnt, button + press)

    print(min_cnt)