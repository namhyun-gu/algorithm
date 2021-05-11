# region Input redirection
import io
import sys

example = """
5
5 4 3 2 1
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())

    receive = [0]
    stack = []

    for idx, tower in enumerate(map(int, input().split())):
        idx += 1

        while stack and tower >= stack[-1][1]:
            stack.pop()

        if stack:
            receive.append(stack[-1][0])
        else:
            receive.append(0)

        stack.append((idx, tower))

    print(" ".join(map(str, receive[1:])))