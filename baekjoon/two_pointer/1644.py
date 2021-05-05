# region Input redirection
import io
import sys

example = """
53
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def eratoshenes_sieve():
    sieve = [1 for _ in range(N + 1)]
    sieve[0] = sieve[1] = 0

    m = int(N ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, N + 1, i):
                sieve[j] = 0

    nums = []
    for num in range(1, N + 1):
        if sieve[num]:
            nums.append(num)
    return nums


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())

    nums = eratoshenes_sieve()

    sum = 0
    lo, hi = 0, 0

    case = 0

    while lo <= hi:
        if sum < N:
            if hi == len(nums):
                break
            sum += nums[hi]
            hi += 1
        elif sum >= N:
            sum -= nums[lo]
            lo += 1

        if sum == N:
            case += 1

    print(case)