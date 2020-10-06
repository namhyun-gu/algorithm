from .. import util

example = """
100 6
"""
util.setinput(example)

# '/'는 실수 나눗셈으로 float으로 반환 (= truediv(a, b))
# '//'는 정수 나눗셈으로 int로 반환 (= floordiv(a, b))
import sys

input = sys.stdin.readline

fact = [0 for _ in range(101)]
fact[0] = fact[1] = 1

for num in range(2, 101):
    fact[num] = num * fact[num - 1]

n, m = map(int, input().split())

print(fact[n] // (fact[m] * fact[n - m]))