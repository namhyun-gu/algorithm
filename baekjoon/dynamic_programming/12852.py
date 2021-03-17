import io
import sys

example = """
10
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())

    dp = [-1 for _ in range(N + 1)]
    dp[1] = 0
    path = [-1 for _ in range(N + 1)]

    for n in range(2, N + 1):
        dp[n] = dp[n - 1] + 1
        path[n] = n - 1

        if n % 2 == 0 and dp[n // 2] + 1 < dp[n]:
            dp[n] = dp[n // 2] + 1
            path[n] = n // 2
        if n % 3 == 0 and dp[n // 3] + 1 < dp[n]:
            dp[n] = dp[n // 3] + 1
            path[n] = n // 3

    print(dp[N])
    while N != -1:
        print(N, end=" ")
        N = path[N]