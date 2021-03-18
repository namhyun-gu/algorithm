import io
import sys

example = """
3
5 3
3 2
2 6
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys

# * Matrix Chain Multiplication
if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    mat = [0 for _ in range(N + 1)]
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for n in range(N):
        mat[n], mat[n + 1] = map(int, input().rstrip().split())

    for len in range(2, N + 1):
        for i in range(1, N - len + 2):
            j = i + len - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                dp[i][j] = min(
                    dp[i][j], dp[i][k] + dp[k + 1][j] + (mat[i - 1] * mat[k] * mat[j])
                )

    print(dp[1][N])