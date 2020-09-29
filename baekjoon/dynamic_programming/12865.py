from .. import util

example = """
4 7
6 13
4 8
3 6
5 12
"""
util.setinput(example)

# Ref: https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem
# Ref(2): https://gsmesie692.tistory.com/113
import sys
input = sys.stdin.readline


def knapsack_problem(weights, values, W, N):
    m = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:  # 없어서 틀렸음.
                m[i][w] = 0
            elif weights[i - 1] > w:
                m[i][w] = m[i - 1][w]
            else:
                m[i][w] = max(
                    m[i - 1][w],
                    m[i - 1][w - weights[i - 1]] + values[i - 1]
                )
    return m[N][W]


N, M = map(int, input().split())
weights = []
values = []
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

print(knapsack_problem(weights, values, M, N))
