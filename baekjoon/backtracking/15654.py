from .. import util

example = """
4 4
1231 1232 1233 1234
"""
util.setinput(example)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))


def n_and_m(n, depth, visited, nums, sequence):
    if depth == M:
        print(sequence)
        return

    for idx, num in enumerate(nums):
        if not visited[idx]:
            visited[idx] = 1
            if len(sequence) == 0:
                next_seq = str(num)
            else:
                next_seq = sequence + " " + str(num)
            n_and_m(n, depth + 1, visited, nums, next_seq)
            visited[idx] = 0


n_and_m(N, 0, [0 for _ in range(N)], sorted(nums), "")
