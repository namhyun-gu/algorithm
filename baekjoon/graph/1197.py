import io
import sys

example = """
3 3
1 2 1
2 3 2
1 3 3
"""
sys.stdin = io.StringIO(example.strip())

# * 최소 신장트리란?
# * 주어진 방향성이 없는 그래프의 서브그래프들 중에서
# * 모든 정점을 포함하는 트리를 의미함.
#
# * 프림과 크루스칼 알고리즘으로 해결할 수 있음.
# ? Ref: https://blog.encrypted.gg/915
import sys
import heapq

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

V, E = map(int, input().split())
group = [-1] * (V + 1)
edges = []

for _ in range(E):
    s, e, w = map(int, input().split())
    heapq.heappush(edges, (w, s, e))


def find(x):
    if group[x] < 0:
        return x
    group[x] = find(group[x])
    return group[x]


def union(u, v):
    u = find(u)
    v = find(v)
    if u == v:
        return False
    if group[u] == group[v]:
        group[u] -= 1
    if group[u] < group[v]:
        group[v] = u
    else:
        group[u] = v
    return True


cnt = 0
ret = 0
while edges:
    w, s, e = heapq.heappop(edges)
    if not union(s, e):
        continue
    ret += w
    cnt += 1
    if cnt == V - 1:
        break

print(ret)