from .. import util

example = """
4 7
20 15 10 17
"""
util.setinput(example)

"""
Parametric Search를 통해 해결하면 되며,
처음 문제를 접근할 때 예제의 정답이 주어지는 배열 내에서 나오기에
right 값을 배열의 위치를 통해 계산했는데 26% 가량에서 틀리게 되었다.

반례를 검색해보니 배열에 모두 같은 값이 주어질 때 이 방식으로
계산을 하게 되면 올바른 답이 나올 수 없다. 따라서 right 값을 tree의 최댓값으로 해야한다.
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
tree = sorted(map(int, input().split()))


def sum_cutting_tree(value):
    sum = 0
    for num in tree:
        if num > value:
            sum += num - value
    return sum


left = 0
right = tree[-1]

result = 0
while left <= right:
    mid = (left + right) // 2
    sum = sum_cutting_tree(mid)
    if sum < M:
        right = mid - 1
    else:
        result = max(result, mid)
        left = mid + 1

print(result)