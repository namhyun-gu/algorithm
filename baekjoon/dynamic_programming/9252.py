import io
import sys

example = """
ACAYKP
CAPCAK
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys

sys.setrecursionlimit(10 ** 4)


def backtrack(dp, a, b, i, j):
    if i == 0 or j == 0:
        return ""
    if a[i - 1] == b[j - 1]:
        return backtrack(dp, a, b, i - 1, j - 1) + a[i - 1]
    if dp[i][j - 1] > dp[i - 1][j]:
        return backtrack(dp, a, b, i, j - 1)
    return backtrack(dp, a, b, i - 1, j)


def lcs(a, b):
    dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif i > 0 and j > 0 and a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            elif i > 0 and j > 0 and a[i - 1] != b[j - 1]:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return backtrack(dp, a, b, len(a), len(b))


if __name__ == "__main__":
    input = sys.stdin.readline

    A = input().rstrip()
    B = input().rstrip()

    result = lcs(A, B)
    print(len(result))
    if result:
        print(result)