import io
import sys

example = """
11
8 3 2 4 8 7 2 4 0 8 8
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    nums = [*map(int, input().split())]
    dp = [[0 for _ in range(21)] for _ in range(N - 1)]

    dp[0][nums[0]] = 1

    for i in range(1, N - 1):
        for j in range(21):
            if dp[i - 1][j] != 0:
                if j + nums[i] in range(21):
                    dp[i][j + nums[i]] += dp[i - 1][j]
                if j - nums[i] in range(21):
                    dp[i][j - nums[i]] += dp[i - 1][j]

    print(dp[N - 2][nums[-1]])