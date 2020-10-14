"""
Parametric Search

가능한 해 구간에 대해서 이분탐색을 하는 방법
보통 가능한 해의 최솟값이나 최댓값을 구하는 문제에서 활용할 수 있는 알고리즘
O(logN)에 해결할 수 있음.


Ref: https://www.crocus.co.kr/1000
Ref (2): https://hongjun7.tistory.com/133
Ref (3): https://ialy1595.github.io/post/parametric-search/
"""


def is_positive(value):
    return value > 0


def search(arr):
    left = 0
    right = len(arr) - 1

    result = 0
    while left <= right:
        mid = (left + right) // 2
        if is_positive(arr[mid]):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


if __name__ == "__main__":
    arr = [-1, -2, -3, -4, -5, -6, 7, 8, 9]
    min_positive = search(arr)
    print(arr[min_positive])