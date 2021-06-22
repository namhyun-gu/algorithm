# region Input redirection
import io
import sys

example = """
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def dfs(graph, src, dest, visit=set(), dist=0):
    if src == dest:
        return dist

    for next in graph[src]:
        if next in visit:
            continue

        visit.add(next)
        ret = dfs(graph, next, dest, visit, dist + 1)
        if ret != -1:
            return ret

    return -1


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    x, y = map(int, input().split())
    m = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = dfs(graph, x, y)
    print(ans)