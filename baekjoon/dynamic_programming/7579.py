import io
import sys

example = """
5 60
30 10 20 35 40
3 0 3 5 4
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def knapsack_problem(memory, costs, N, M):
    total_cost = sum(costs)
    dp = [[0 for _ in range(total_cost + 1)] for _ in range(N + 1)]

    for index in range(1, N + 1):
        for cost in range(total_cost + 1):
            if cost - costs[index] >= 0:
                dp[index][cost] = max(
                    dp[index][cost], dp[index - 1][cost - costs[index]] + memory[index]
                )

            dp[index][cost] = max(dp[index][cost], dp[index - 1][cost])

    for cost in range(total_cost + 1):
        if dp[N][cost] >= M:
            return cost
    return total_cost


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    memory = [0, *map(int, input().split())]
    costs = [0, *map(int, input().split())]

    print(knapsack_problem(memory, costs, N, M))