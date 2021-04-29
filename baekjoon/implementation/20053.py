# region Input redirection
import io
import sys

example = """
3
5
20 28 22 25 21
5
30 21 17 25 29
5
20 10 35 30 7
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        _ = int(input())
        nums = sorted(list(map(int, input().split())))

        print(nums[0], nums[-1])