from .. import util

example = """
mirkovC4nizCC44
C4
"""
util.setinput(example)

"""
이 문제를 deque를 통해 스택 내용을 앞부터 비교하여 문자열과 같다면
해당 문자열만큼 스택을 pop하고 그렇지 않다면 다음 문자를 시작으로 문자열을 비교하였는데
이 방식대로 문제를 풀 경우 시간초과가 발생

그렇게 할 필요없이 입력 문자열을 스택에 추가할 때
비교 문자열 크기보다 크거나 같다면 스택의 끝부터, 비교 문자열의 끝을 비교하여
모두 같다면 길이만큼 pop해도 문제를 해결할 수 있다.

앞에서부터 비교하지 않고 뒤에서 비교하는 방법으로 풀면 해결할 수 있었던 문제

Ref: https://ksshlee.github.io/baekjoon/백준-9935-문자열-폭발/
"""
import sys

input = sys.stdin.readline

string = input().rstrip()
bomb = input().rstrip()

stack = []


for c in string:
    stack.append(c)

    if len(stack) >= len(bomb):
        is_same = True
        for idx in range(1, len(bomb) + 1):
            if stack[-idx] != bomb[-idx]:
                is_same = False
                break
        if is_same:
            for _ in range(len(bomb)):
                stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))