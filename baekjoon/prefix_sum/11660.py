from .. import util

example = """
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
"""
util.setinput(example)

# Ref: https://chanhuiseok.github.io/posts/baek-19/
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

table = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
sum = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        table[i + 1][j + 1] = line[j]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - \
            sum[i - 1][j - 1] + table[i][j]

for m in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    result = sum[y2][x2] - (sum[y2][x1 - 1] + sum[y1 - 1]
                            [x2]) + sum[y1 - 1][x1 - 1]
    print(result)
