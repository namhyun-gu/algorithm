import io
import sys

example = """
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
def countSwaps(a):
    swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


if __name__ == "__main__":
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
