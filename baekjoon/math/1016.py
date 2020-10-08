from .. import util

example = """
1000000000000 1000001000000
"""
util.setinput(example)

"""
Ref: https://ko.wikipedia.org/wiki/에라토스테네스의_체
Ref (2): https://chanhuiseok.github.io/posts/baek-16/
"""
import sys

input = sys.stdin.readline

min, max = map(int, input().split())

# min 값이 1,000,000,000,000도 가능하므로 max에서 빼주지 않으면 MemoryError가 발생한다.
sieve = [False for _ in range(max - min + 1)]
cnt = 0

i = 2
while i * i <= max:
    start = min // (i * i)
    if min % (i * i) != 0:
        start += 1

    while start * (i * i) <= max:
        if not sieve[start * (i * i) - min]:
            sieve[start * (i * i) - min] = True
            cnt += 1
        start += 1
    i += 1

print((max - min + 1) - cnt)
