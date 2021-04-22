def solution(triangle):
    N = len(triangle)
    dp = [[0 for _ in range(N)] for _ in range(N)]

    for n in range(N):
        dp[N - 1][n] = triangle[N - 1][n]

    for i in range(N - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

    return dp[0][0]