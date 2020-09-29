from .. import util

example = """
ACAYKP
CAPCAK
"""
util.setinput(example)

# Ref: https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
# Ref(2) : https://algorithm-visualizer.org/dynamic-programming/longest-common-subsequence
import sys
sys.setrecursionlimit(10 ** 4)  # 재귀 사용 시 런타임 에러가 난다면 추가
input = sys.stdin.readline

A = input().strip()
B = input().strip()


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


print(len(lcs(A, B)))
