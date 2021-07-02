# region Input redirection
import io
import sys

example = """
5
8*3+5
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def calculate(op1, operator, op2):
    if operator == "+":
        return op1 + op2
    elif operator == "-":
        return op1 - op2
    else:
        return op1 * op2


def dfs(value, index=0):
    global answer

    if index >= len(operator):
        answer = max(answer, value)
        return

    no_bracket_val = calculate(value, operator[index], operand[index + 1])
    dfs(no_bracket_val, index + 1)

    if index + 1 < len(operator):
        in_bracket = calculate(
            operand[index + 1], operator[index + 1], operand[index + 2]
        )
        bracket_val = calculate(value, operator[index], in_bracket)
        dfs(bracket_val, index + 2)


if __name__ == "__main__":
    input = sys.stdin.readline

    N = input()

    answer = -sys.maxsize
    operand = []
    operator = []

    for idx, ch in enumerate(input().rstrip()):
        if idx % 2:
            operator.append(ch)
        else:
            operand.append(int(ch))

    dfs(operand[0])
    print(answer)