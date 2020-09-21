from .. import util

example = """
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""
util.setinput(example)

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 1e7 = 1 * 10^7
def floyd_warshall():
    costs = [[1e7 for _ in range(N + 1)] for _ in range(N + 1)]

    for s in range(1, N + 1):
        for e, w in graph[s]:
            costs[s][e] = min(costs[s][e], w)

    for k in range(1, N + 1):
        for s in range(1, N + 1):
            for e in range(1, N + 1):
                if s == e:
                    costs[s][e] = 0
                else:
                    costs[s][e] = min(costs[s][e], costs[s][k] + costs[k][e])
    return costs


costs = floyd_warshall()
for s in range(1, N + 1):
    for e in range(1, N + 1):
        if costs[s][e] == 1e7:
            print(0, end=" ")
        else:
            print(costs[s][e], end=" ")
    print()
