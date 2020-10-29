"""
최대공약수

최대공약수는 유클리드 호제법을 이용하여
a와 b의 최대공약수가 (a, b)이고,
a를 b로 나눈 나머지가 r일때

(a, b) = (b, r) 임의 성질을 이용하여 구할 수 있다.

---

최소공배수

최소공배수는 최대공약수를 활용하여 구할 수 있다.

lcm(a, b) = a * b / gcd(a, b)
"""


def gcd(a, b):
    while b != 0:
        mod = a % b
        a = b
        b = mod
    return a


def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)