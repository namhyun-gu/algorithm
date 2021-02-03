from math import inf


def solution(n, s, a, b, fares):
    dist = [[inf for _ in range(n + 1)] for _ in range(n + 1)]

    for c, d, f in fares:
        dist[c][d] = dist[d][c] = f

    for i in range(1, n + 1):
        dist[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    answer = inf
    for k in range(1, n + 1):
        answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])
    return answer


if __name__ == "__main__":
    ret = solution(
        6,
        4,
        6,
        2,
        [
            [4, 1, 10],
            [3, 5, 24],
            [5, 6, 2],
            [3, 1, 41],
            [5, 1, 24],
            [4, 6, 50],
            [2, 4, 66],
            [2, 3, 22],
            [1, 6, 25],
        ],
    )
    print(ret)

    ret = solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
    print(ret)

    ret = solution(
        6,
        4,
        5,
        6,
        [
            [2, 6, 6],
            [6, 3, 7],
            [4, 6, 7],
            [6, 5, 11],
            [2, 5, 12],
            [5, 3, 20],
            [2, 4, 8],
            [4, 3, 9],
        ],
    )
    print(ret)