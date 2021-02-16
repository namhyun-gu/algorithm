import io
import sys

example = """
2
5
2 1 5 3 4
5
2 5 1 3 4
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
def minimumBribes(q):
    ret = 0

    for i, p in enumerate(q):
        p -= 1

        if p - i > 2:
            print("Too chaotic")
            return

        for j in range(max(0, p - 1), i):
            if p < q[j]:
                ret += 1

    print(ret)


if __name__ == "__main__":
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
