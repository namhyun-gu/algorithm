"""
이 문제를 처음 접근할 떄 그림에서 이와 같은 패턴을 발견할 수 있었다.
2 * 3인 사각형에 대해 대각선으로 나눌 경우

X O
X X
O X

다음과 같이 4개의 사각형을 못 쓴다는 것을 알 수 있어서
단순히 W와 H가 각각 2의 배수, 3의 배수일때
전체 사각형의 개수에서 W // 2 한 값에 4를 곱한 값을 빼주는 식으로
문제를 풀었으나 해결되지 않았다.

문제에 대해 검색해보니 최대공약수로 해결할 수 있다고 하여
최대공약수를 이용하여 구하니 해결은 되었으나

어떤 방법을 통해 최대공약수를 유추할 수 있는 것인지는 잘 모르겠다.

Ref: https://leedakyeong.tistory.com/entry/프로그래머스-멀쩡한-사각형-in-python
"""
def gcd(a, b):
    while b != 0:
        mod = a % b
        a = b
        b = mod
    return a


def solution(w, h):
    return w * h - (w + h - gcd(w, h))


if __name__ == "__main__":
    assert solution(8, 12) == 80