def shift(s, n):
    temp = s
    for _ in range(n):
        temp = temp[1:] + temp[0]
    return temp


def is_correct(s):
    stack = []

    for c in s:
        if c in ["[", "(", "{"]:
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                top = stack[-1]
                if top == "[" and c == "]":
                    stack.pop()
                elif top == "(" and c == ")":
                    stack.pop()
                elif top == "{" and c == "}":
                    stack.pop()
                else:
                    return False
    return len(stack) == 0


def solution(s):
    answer = 0
    for n in range(len(s) - 1):
        temp = shift(s, n)
        if is_correct(temp):
            answer += 1
    return answer