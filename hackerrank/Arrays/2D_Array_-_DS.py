import io
import sys

example = """
-1 1 -1 0 0 0
0 -1 0 0 0 0
-1 -1 -1 0 0 0
0 -9 2 -4 -4 0
-7 0 0 -2 0 0
0 0 -1 -2 -4 0
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
hourglass = [
    (0, 0),
    (1, 0),
    (2, 0),
    (1, 1),
    (0, 2),
    (1, 2),
    (2, 2),
]


def hourglassSum(arr):
    ret = None
    for r in range(len(arr) - 2):
        for c in range(len(arr) - 2):
            sum = 0
            for tr, tc in hourglass:
                sum += arr[c + tc][r + tr]
            if ret == None or ret < sum:
                ret = sum
    return ret


if __name__ == "__main__":
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)