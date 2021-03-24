def solution(n, times):
    left, right = 1, times[-1] * n
    ans = right

    while left <= right:
        middle = (left + right) // 2

        counts = 0
        for time in times:
            counts += middle // time

        if counts < n:
            left = middle + 1
        else:
            ans = min(ans, middle)
            right = middle - 1

    return ans


if __name__ == "__main__":
    # ret = solution(6, [7, 10])

    ret = solution(1000000000, [1, 1000000000])
    print(ret)