import io
import sys

example = """
8 8
1 7
3 7
4 7
3 4
4 6
3 5
0 4
2 7
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys

sys.setrecursionlimit(10 ** 6)


def connect(graph, cur, depth):
    global can_conn

    visit.add(cur)

    if depth == 4:
        can_conn = True
        return

    for next in graph[cur]:
        if next not in visit:
            connect(graph, next, depth + 1)
            visit.remove(next)
            if can_conn:
                return


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    can_conn = False
    visit = set()

    for n in range(N):
        connect(graph, n, 0)
        visit.remove(n)
        if can_conn:
            break
    print(1 if can_conn else 0)