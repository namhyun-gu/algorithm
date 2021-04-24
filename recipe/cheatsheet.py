import sys

# 최단 거리
# - 하나의 정점에서 다른 정점 간 최단거리
#   간선 가중치 X : BFS
#   음수 가중치 : Bellman-Ford
#   둘다 아님 : Dijkstra
# - 모든 정점 간 최단 거리 : Floyd warshall
inf = sys.maxsize

graph = [
    [0, 7, inf, inf, 3, 10, inf],
    [7, 0, 4, 10, 2, 6, inf],
    [inf, 4, 0, 2, inf, inf, inf],
    [inf, 10, 2, 0, 11, 9, 4],
    [3, 2, inf, 11, 0, inf, 5],
    [10, 6, inf, 9, inf, 0, inf],
    [inf, inf, inf, 4, 5, inf, 0],
]

N = 7


def bellman_ford(start):
    dist = [inf for _ in range(N)]
    dist[start] = 0

    prev = [None for _ in range(N)]

    edges = []
    for i in range(N):
        for j in range(N):
            if i != j and graph[i][j] != inf:
                edges.append((i, j, graph[i][j]))

    for _ in range(N - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            # 음수 가중치 존재
            pass

    return dist, prev


import heapq


def dijkstra(start):
    dist = [inf for _ in range(N)]
    dist[start] = 0

    prev = [None for _ in range(N)]

    heap = []
    for n in range(N):
        heapq.heappush(heap, (dist[n], n))

    while heap:
        _, u = heapq.heappop(heap)

        for v, w in enumerate(graph[u]):
            if w == inf:
                continue

            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))

    return dist, prev


def path(prev, start, dest):
    path = []
    u = dest
    while prev[u]:
        path.append(u)
        u = prev[u]
    path.append(start)
    return path


def floyd_warshall():
    dist = [[graph[i][j] for j in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


dist, prev = bellman_ford(1)
print(dist)
print(" -> ".join(map(str, path(prev, 1, 6))))

dist, prev = dijkstra(1)
print(dist)
print(" -> ".join(map(str, path(prev, 1, 6))))

dist = floyd_warshall()
for i in range(N):
    print(i, " -> ", dist[i])

# MST : Kruskal
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N = 8
parent = [i for i in range(N)]
edges = [
    (1, 7, 12),
    (1, 4, 28),
    (1, 2, 67),
    (1, 5, 17),
    (2, 4, 24),
    (2, 5, 62),
    (3, 5, 20),
    (3, 6, 37),
    (4, 7, 13),
    (5, 6, 45),
    (5, 7, 73),
]


edges.sort(key=lambda edge: edge[2])

mst_cost = 0
mst_path = []

for u, v, w in edges:
    if find(parent, u) != find(parent, v):
        union(parent, u, v)
        mst_path.append((u, v))
        mst_cost += w

print(mst_cost)
print(mst_path)

# Topological sort
import collections

N = 4

graph = [[] for _ in range(N + 1)]

#       2
# 1 ->      -> 4
#       3
edges = [(1, 2), (1, 3), (2, 4), (3, 4)]

indegrees = [0 for _ in range(N + 1)]

for u, v in edges:
    graph[u].append(v)
    indegrees[v] += 1


def topological_sort():
    queue = collections.deque()

    for v in range(1, len(indegrees)):
        if indegrees[v] == 0:
            queue.append(v)

    while queue:
        cur = queue.popleft()

        print(cur, "->", end=" ")

        for next in graph[cur]:
            indegrees[next] -= 1
            if indegrees[next] == 0:
                queue.append(next)
    print()


topological_sort()

# Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def find(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end_of_word


trie = Trie()
trie.insert("ABC")
print(trie.find("ABC"))
print(trie.find("BC"))