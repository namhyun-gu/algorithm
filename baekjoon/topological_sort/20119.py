# region Input redirection
import io
import sys

example = """
7 6
3 1 5 7 2
3 1 3 6 7
2 3 4 5
2 4 5 3
2 5 6 4
5 1 2 4 5 6 3
3
1 5 6
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import collections


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())

    dep = [[] for _ in range(N + 1)]
    indegree = [0 for _ in range(N + 1)]
    contain = [0 for _ in range(N + 1)]
    target = [0 for _ in range(M + 1)]

    for m in range(1, M + 1):
        k, *x, r = map(int, input().split())
        indegree[m] = k
        for i in x:
            dep[i].append(m)
        target[m] = r

    L = int(input())
    potion = list(map(int, input().split()))

    queue = collections.deque()

    for item in potion:
        if contain[item]:
            continue
        contain[item] = 1
        for next in dep[item]:
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(target[next])

    while queue:
        cur = queue.popleft()
        if contain[cur]:
            continue
        contain[cur] = 1
        for next in dep[cur]:
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(target[next])

    print(sum(contain))
    for i in range(1, N + 1):
        if contain[i]:
            print(i, end=" ")
