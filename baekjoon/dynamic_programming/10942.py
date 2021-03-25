import io
import sys

example = """
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7
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

    dp = [[0 for _ in range(N)] for _ in range(N)]

    for n in range(N):
        dp[n][n] = 1

    for l in range(N):
        for s in range(N - l):
            e = s + l

            if s != e:
                if s + 1 == e:  # 두 글자일때를 생각 못해서 틀렸음 ㅋ
                    if nums[s] == nums[e]:
                        dp[s][e] = 1
                    else:
                        dp[s][e] = 0
                else:
                    if nums[s] == nums[e] and dp[s + 1][e - 1]:
                        dp[s][e] = 1
                    else:
                        dp[s][e] = 0

    M = int(input())
    for _ in range(M):
        s, e = map(int, input().split())
        s -= 1
        e -= 1

        if dp[s][e]:
            print(1)
        else:
            print(0)
