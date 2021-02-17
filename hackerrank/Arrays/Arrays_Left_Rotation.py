import io
import sys

example = """
5 4
1 2 3 4 5
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
def rotLeft(a, d):
    return a[d:] + a[:d]


if __name__ == "__main__":
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)