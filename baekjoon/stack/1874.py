from .. import util

example = """
8
4
3
6
8
7
5
2
1
"""
util.setinput(example)

"""
이 문제를 풀때
주어지는 수열을 반대로 뒤집어서 수열의 내용을 순차적으로 탐색하면서
현재 넣어야되는 숫자와 비교하여 같다면 스택에 추가하고, 다음 수열의 숫자, 다음 숫자로 넘어가고
그렇지 않다면 해당 수열의 숫자까지 반복하여 스택에 추가하고,
수열에서 N이 나올때까지 오름차순이면 가능, 그렇지 않다면 불가능한 식으로 풀어보려 했는데
pop을 하는 경우에 대해 처리하는 것이 모호하여 솔루션을 검색했다.

이 솔루션에서는
스택에 1...N 까지 숫자를 추가하고,
스택의 top이 현재 비교할 수열의 수와 같다면 pop을 반복하는 식으로 해결한다.

Ref: https://sihyungyou.github.io/baekjoon-1874/
"""
import sys

input = sys.stdin.readline

N = int(input())
sequence = []
for _ in range(N):
    sequence.append(int(input()))

stack = []
operations = []

idx = 0
for num in range(1, N + 1):
    stack.append(num)
    operations.append("+")

    while len(stack) > 0 and stack[-1] == sequence[idx]:
        stack.pop()
        operations.append("-")
        idx += 1

if len(stack) > 0:
    print("NO")
else:
    for operation in operations:
        print(operation)