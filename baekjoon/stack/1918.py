from .. import util

example = """
(A+(B*C))-(D/E)
"""
util.setinput(example)

# Ref: https://summer-story.tistory.com/13
import sys
input = sys.stdin.readline

expression = input().rstrip()


def post_notation(expression):
    result = ""
    stack = []
    for c in expression:
        if c == '*' or c == '/':
            if len(stack) != 0 and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(c)
        elif c == '+' or c == '-':
            while stack:
                top = stack[-1]
                if top == '(':
                    break
                result += stack.pop()
            stack.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            result += c
    while stack:
        result += stack.pop()
    return result


result = post_notation(expression)
print(result)
