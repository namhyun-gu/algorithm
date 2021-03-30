import io
import sys
from typing import Counter

example = """
5
ABC*+DE/-
1
2
3
4
5
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def to_value(ch, operands):
    return operands[ord(ch) - ord("A")]


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    expression = input().rstrip()
    operands = [int(input()) for _ in range(N)]

    stack = []
    for ch in expression:
        if ch not in ["+", "-", "*", "/"]:
            stack.append(to_value(ch, operands))
        else:
            b = stack.pop()
            a = stack.pop()

            if ch == "+":
                stack.append(a + b)
            elif ch == "-":
                stack.append(a - b)
            elif ch == "*":
                stack.append(a * b)
            elif ch == "/":
                stack.append(a / b)

    print(format(stack[-1], ".2f"))