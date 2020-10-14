"""
Binary Search (= 이분탐색)

오름차순으로 정렬된 리스트에서 특정한 값을 찾는 알고리즘

Ref: https://ko.wikipedia.org/wiki/이진_검색_알고리즘
"""


def search(arr, value):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > value:
            right = mid - 1
        elif arr[mid] < value:
            left = mid + 1
        else:
            return 1
    return 0


def search_recursive(arr, value, left, right):
    if left > right:
        return 0

    mid = (left + right) // 2
    if arr[mid] > value:
        return search_recursive(arr, value, left, mid - 1)
    elif arr[mid] < value:
        return search_recursive(arr, value, mid + 1, right)
    return 1


if __name__ == "__main__":
    arr = sorted([1, 5, 3, 7, 2, 9, 4])
    key = 3

    exists = search(arr, key)
    if exists:
        print(f"Found {key}")
    else:
        print(f"Not found {key}")

    exists = search_recursive(arr, key, 0, len(arr) - 1)
    if exists:
        print(f"Found {key}")
    else:
        print(f"Not found {key}")