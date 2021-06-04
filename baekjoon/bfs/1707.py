# region Input redirection
import io
import sys

example = """
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import collections

RED = 0
BLUE = 1


def is_bi_graph(graph):
    color = [-1] * V

    for v in range(1, V):
        if color[v] == -1:
            fill_color(graph, color, v)

    for u in range(1, V):
        for v in graph[u]:
            if color[u] == color[v]:
                return False
    return True


def fill_color(graph, color, v):
    queue = collections.deque()
    queue.append(v)

    color[v] = RED

    while queue:
        cur = queue.popleft()

        for next in graph[cur]:
            if color[next] == -1:
                color[next] = (color[cur] + 1) % 2
                queue.append(next)


if __name__ == "__main__":
    input = sys.stdin.readline

    K = int(input())

    for _ in range(K):
        V, E = map(int, input().split())
        V += 1

        graph = [[] for _ in range(V)]

        for _ in range(E):
            s, e = map(int, input().split())

            graph[s].append(e)
            graph[e].append(s)

        if is_bi_graph(graph):
            print("YES")
        else:
            print("NO")