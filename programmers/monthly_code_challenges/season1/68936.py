def can_compress(arr, start_r, start_c, size):
    first = arr[start_r][start_c]
    for r in range(start_r, start_r + size):
        for c in range(start_c, start_c + size):
            if arr[r][c] != first:
                return (False, 0)
    return (True, first)


def add_arr(a, b):
    for i in range(len(a)):
        a[i] += b[i]


def compress(arr, r, c, size):
    result = [0, 0]

    if size == 1:
        result[arr[r][c]] += 1
        return result

    available, n = can_compress(arr, r, c, size)
    if available:
        result[n] += 1
        return result
    else:
        half = size // 2
        add_arr(result, compress(arr, r, c, half))
        add_arr(result, compress(arr, r + half, c, half))
        add_arr(result, compress(arr, r, c + half, half))
        add_arr(result, compress(arr, r + half, c + half, half))
        return result


def solution(arr):
    return compress(arr, 0, 0, len(arr))


if __name__ == "__main__":
    assert solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]) == [4, 9]
    assert (
        solution(
            [
                [1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 1, 1, 1],
                [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1],
            ]
        )
        == [10, 15]
    )
