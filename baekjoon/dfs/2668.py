import io
import sys

example = """
7
3
1
1
5
5
4
6
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def check_cycle(src, dest):
    global cycle
    global nums

    if not cycle[src]:
        cycle[src] = 1
        check_cycle(table[src], dest)
    else:
        if src == dest:
            nums.append(src)


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())

    table = [0, *[int(input()) for _ in range(N)]]

    nums = []
    for r in range(1, N + 1):
        cycle = [0 for _ in range(N + 1)]
        check_cycle(r, r)

    print(len(nums))
    print("\n".join(map(str, nums)))