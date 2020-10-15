"""
에라토스테네스의 체

2부터 - N의 제곱근까지의 배수인 수를 걸러 소수만 남김

Ref: https://ko.wikipedia.org/wiki/에라토스테네스의_체
"""
N = 100

sieve = [1 for _ in range(N + 1)]
sieve[0] = sieve[1] = 0

m = int(N ** 0.5)
for i in range(2, m + 1):
    if sieve[i]:
        for j in range(i + i, N + 1, i):
            sieve[j] = 0


for num in range(1, N + 1):
    if sieve[num]:
        print(num)