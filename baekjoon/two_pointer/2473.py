import io
import sys

example = """
4
-5 2 3 4
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    liquid = sorted([*map(int, input().rstrip().split())])

    total = sys.maxsize
    result = 0, 0, 0

    for mid in range(1, N - 1):
        l, r = 0, N - 1
        while l < mid < r:
            sum = liquid[l] + liquid[mid] + liquid[r]

            if abs(sum) < total:
                total = abs(sum)
                result = liquid[l], liquid[mid], liquid[r]
            elif sum < 0:
                l += 1
            else:
                r -= 1

    print(" ".join(map(str, result)))