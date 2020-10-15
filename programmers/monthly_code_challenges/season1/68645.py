def draw_triangle(triangle, num, start_r, start_c, size):
    if size == 1:
        triangle[start_r][start_c] = num
    else:
        for r in range(size):
            triangle[start_r + r][start_c] = num
            num += 1

        for c in range(1, size):
            triangle[start_r + r][start_c + c] = num
            num += 1

        for d in reversed(range(1, size - 1)):
            triangle[start_r + d][start_c + d] = num
            num += 1

        if size > 3:
            draw_triangle(triangle, num, start_r + 2, start_c + 1, size - 3)


def solution(n):
    triangle = [[0 for _ in range(n)] for _ in range(n)]
    answer = []
    draw_triangle(triangle, 1, 0, 0, n)

    for r in range(n):
        for c in range(n):
            if triangle[r][c] > 0:
                answer.append(triangle[r][c])
    return answer


if __name__ == "__main__":
    assert solution(1) == [1]
    assert solution(4) == [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]
    assert solution(5) == [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9]
    assert solution(6) == [
        1,
        2,
        15,
        3,
        16,
        14,
        4,
        17,
        21,
        13,
        5,
        18,
        19,
        20,
        12,
        6,
        7,
        8,
        9,
        10,
        11,
    ]
