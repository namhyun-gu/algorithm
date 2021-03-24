def solution(n, results):
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for a, b in results:
        graph[a][b] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True

    answer = 0
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if graph[i][j] or graph[j][i]:
                cnt += 1
        if cnt == n - 1:
            answer += 1
    return answer


if __name__ == "__main__":
    ret = solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
    print(ret)