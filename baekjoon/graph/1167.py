from .. import util
example = """
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
"""
util.setinput(example)

V = int(input())
graph = [[] for _ in range(V)]
for _ in range(V):
    line = list(map(int, input().split()))
    for i in range(1, len(line) - 1, 2):
        graph[line[0] - 1].append((line[i] - 1, line[i + 1]))


def dfs(graph, start, dists):
    for v, dist in graph[start]:
        if dists[v] == 0:
            dists[v] = dists[start] + dist
            dfs(graph, v, dists)


dists = [0 for _ in range(V)]
dfs(graph, 0, dists)

max_v = (0, 0)
for idx, dist in enumerate(dists):
    if dist > max_v[1]:
        max_v = (idx, dist)

dists = [0 for _ in range(V)]
dfs(graph, max_v[0], dists)
dists[max_v[0]] = 0
print(max(dists))
