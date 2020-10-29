from .. import util

example = """
5 2
"""
util.setinput(example)

"""
Ref: https://ko.wikipedia.org/wiki/이항_계수
"""
import sys
from math import factorial

input = sys.stdin.readline

N, K = map(int, input().split())

if 0 <= K <= N:
    print(factorial(N) // (factorial(K) * factorial(N - K)))
elif K < 0 or K > N:
    print(0)