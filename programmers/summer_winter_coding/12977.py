import itertools


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    for picks in itertools.combinations(nums, 3):
        if is_prime(sum(picks)):
            answer += 1
    return answer


if __name__ == "__main__":
    assert solution([1, 2, 3, 4]) == 1
    assert solution([1, 2, 7, 6, 4]) == 4