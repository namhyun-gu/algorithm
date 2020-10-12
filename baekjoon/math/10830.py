from .. import util

example = """
3 3
1 2 3
4 5 6
7 8 9
"""
util.setinput(example)

"""
아래 방법으로 곱셈은 구했으나 이것을 통해 여러번 곱하는 걸로
원하는 답을 얻을 수 없어서 행렬 곱셈 방식이 잘못되었나 싶어
*슈트라센 알고리즘을 통해 구현을 시도했으나 행렬을 다루기가 까다로워 포기했음.

알고보니 곱셈을 구할 때 매 곱셈마다 나머지를 구하지 않아서 값이 나오지 않았던 거였고
여러번 곱을 하는것이 아닌 분할정복을 이용한 거듭제곱 방식으로 문제를 풀면 해결할 수 있었음

Ref: https://imnotabear.tistory.com/5
"""
import sys
import copy

input = sys.stdin.readline

N, B = map(int, input().split())

matrix = [[0 for _ in range(N)] for _ in range(N)]

for r in range(N):
    line = list(map(int, input().split()))
    for c in range(N):
        matrix[r][c] = line[c]


def multiple(a, b):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for i in range(N):
                result[r][c] += a[r][i] * b[i][c]
                result[r][c] %= 1000
    return result


def pow(a, b, n):
    if n == 1:
        return b
    if n % 2 == 0:
        result = pow(a, b, n // 2)
        return multiple(result, result)
    result = pow(a, b, n - 1)
    return multiple(result, a)


answer = copy.deepcopy(matrix)
answer = pow(answer, matrix, B)
for r in range(N):
    for c in range(N):
        print(answer[r][c] % 1000, end=" ")
    print()
