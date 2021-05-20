# region Input redirection
import io
import sys

example = """
3
<<BP<A>>Cd-
ThIsIsS3Cr3t
-A-
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        case = input().rstrip()

        left = deque()
        right = deque()

        for c in case:
            if c == "<":
                if left:
                    right.appendleft(left.pop())
            elif c == ">":
                if right:
                    left.append(right.popleft())
            elif c == "-":
                if left:
                    left.pop()
            else:
                left.append(c)

        print("".join([*left, *right]))
