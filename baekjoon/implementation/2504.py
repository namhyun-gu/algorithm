# region Input redirection
import io
import sys

example = """
(()[[]])([])
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def is_correct(expression):
    stack = []

    for c in expression:
        if c in ["(", "["]:
            stack.append(c)
        elif c == ")":
            if len(stack) == 0:
                return False

            if stack.pop() != "(":
                return False
        elif c == "]":
            if len(stack) == 0:
                return False

            if stack.pop() != "[":
                return False

    return len(stack) == 0


def evaluate(expression):
    stack = []

    for c in expression:
        temp = 0

        if c in ["(", "["]:
            stack.append(c)
        elif c == ")":
            while stack and stack[-1] != "(":
                temp += stack.pop()
            stack.pop()

            if temp == 0:
                stack.append(2)
            else:
                stack.append(2 * temp)
        elif c == "]":
            while stack and stack[-1] != "[":
                temp += stack.pop()
            stack.pop()

            if temp == 0:
                stack.append(3)
            else:
                stack.append(3 * temp)

    return sum(stack)


if __name__ == "__main__":
    input = sys.stdin.readline
    expression = input().rstrip()

    if not is_correct(expression):
        print(0)
    else:
        print(evaluate(expression))