def convert(n, from_base, to_base):
    idx = 0
    result = 0
    while n > 0:
        result += (n % to_base) * pow(from_base, idx)
        n //= to_base
        idx += 1
    return result


def solution(n):
    answer = convert(n, 10, 3)
    answer = int(str(answer)[::-1])
    answer = convert(answer, 3, 10)
    return answer


if __name__ == "__main__":
    assert solution(45) == 7
    assert solution(125) == 229