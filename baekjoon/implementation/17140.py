# region Input redirection
import io
import sys

example = """
3 3 3
1 1 1
1 1 1
1 1 1
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import functools


def compare(item_a, item_b):
    if item_a[1] < item_b[1]:
        return -1
    elif item_a[1] > item_b[1]:
        return 1
    else:
        if item_a[0] < item_b[0]:
            return -1
        else:
            return 1


def sort(arr):
    d = {}
    for num in arr:
        if num != 0:
            d.setdefault(num, 0)
            d[num] += 1

    ret = []
    for item in sorted(d.items(), key=functools.cmp_to_key(compare)):
        ret.extend(item)
    return ret


def R(arr):
    temp = []
    for row in range(len(arr)):
        temp.append(sort(arr[row]))

    max_size = 0
    for row in range(len(temp)):
        max_size = max(max_size, len(temp[row]))

    for row in range(len(temp)):
        if len(temp[row]) < max_size:
            size = len(temp[row])
            for _ in range(max_size - size):
                temp[row].append(0)
    return temp


def C(arr):
    arr_t = list(zip(*arr))
    return list(zip(*R(arr_t)))


def clip(arr):
    temp = [[arr[r][c] for c in range(100)] for r in range(100)]
    return temp


if __name__ == "__main__":
    input = sys.stdin.readline

    r, c, k = map(int, input().split())
    r -= 1
    c -= 1

    arr = [list(map(int, input().split())) for _ in range(3)]

    t = 0
    while t <= 100:
        row = len(arr)
        col = len(arr[0])

        if r in range(row) and c in range(col) and arr[r][c] == k:
            print(t)
            exit(0)

        if row >= col:
            arr = R(arr)
        else:
            arr = C(arr)

        if row > 100 or col > 100:
            arr = clip(arr)

        t += 1

    print(-1)