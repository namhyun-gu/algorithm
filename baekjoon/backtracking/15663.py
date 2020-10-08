from .. import util

example = """
3 1
4 4 2
"""
util.setinput(example)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

sequence_set = set()


def n_and_m(n, depth, visited, nums, sequence):
    if depth == M:
        sequence_set.add(" ".join(map(str, sequence)))
        return

    for idx, num in enumerate(nums):
        if not visited[idx]:
            visited[idx] = 1
            if len(sequence) == 0:
                next_seq = [num]
            else:
                next_seq = [*sequence, num]
            n_and_m(n, depth + 1, visited, nums, next_seq)
            visited[idx] = 0


n_and_m(N, 0, [0 for _ in range(N)], sorted(nums), [])


sequences = []
for sequence in sequence_set:
    sequences.append(list(map(int, sequence.split())))

for sequence in sorted(sequences):
    print(" ".join(map(str, sequence)))