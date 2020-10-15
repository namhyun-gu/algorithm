import itertools


def solution(numbers):
    result = set()
    for picked in itertools.permutations(numbers, 2):
        sum = 0
        for num in picked:
            sum += num
        result.add(sum)
    return sorted(result)


if __name__ == "__main__":
    assert solution([2, 1, 3, 4, 1]) == [2, 3, 4, 5, 6, 7]
    assert solution([5, 0, 2, 7]) == [2, 5, 7, 9, 12]