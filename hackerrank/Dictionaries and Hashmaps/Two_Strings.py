import io
import sys

example = """
2
hello
world
hi
world
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
def twoStrings(s1, s2):
    s1_set = set(s1)
    ret = False
    for c in s2:
        if c in s1_set:
            ret = True
    return "YES" if ret else "NO"


if __name__ == "__main__":
    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)
        print(result)