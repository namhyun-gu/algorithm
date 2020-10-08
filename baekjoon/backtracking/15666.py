from .. import util

example = """
4 4
1 1 2 2
"""
util.setinput(example)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

sequence_set = set()


def n_and_m(n, depth, nums, sequence):
    if depth == M:
        sequence_set.add(" ".join(map(str, sequence)))
        return

    for num in nums:
        if len(sequence) == 0:
            next_seq = [num]
        else:
            if sequence[-1] > num:
                continue
            next_seq = [*sequence, num]
        n_and_m(n, depth + 1, nums, next_seq)


n_and_m(N, 0, sorted(nums), [])


sequences = []
for sequence in sequence_set:
    sequences.append(list(map(int, sequence.split())))

for sequence in sorted(sequences):
    print(" ".join(map(str, sequence)))