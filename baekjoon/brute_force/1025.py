import io
import sys

example = """
2 3
123
456
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import math


def is_square(num):
    s = int(math.sqrt(num))
    return s * s == num


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    board = [input().rstrip() for _ in range(N)]

    ret = -1
    for n in range(N):
        for m in range(M):
            for col_d in range(-N, N):
                for row_d in range(-M, M):
                    if col_d == 0 and row_d == 0:
                        continue

                    temp_n = n
                    temp_m = m
                    nums = ""
                    while temp_n in range(N) and temp_m in range(M):
                        nums += board[temp_n][temp_m]
                        if is_square(int(nums)):
                            ret = max(ret, int(nums))

                        temp_n += col_d
                        temp_m += row_d

                    if is_square(int(nums)):
                        ret = max(ret, int(nums))

    print(ret)