from .. import util

example = """
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
"""
util.setinput(example)

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start, end = map(int, input().split())


def dijkstra(start):
    costs = [1e9] * (n + 1)
    costs[start] = 0
    routes = [0] * (n + 1)
    queue = []
    heappush(queue, (0, start))

    while queue:
        cost, u = heappop(queue)
        for e, c in graph[u]:
            if costs[e] > c + cost:
                costs[e] = c + cost
                routes[e] = u
                heappush(queue, (costs[e], e))
    return (routes, costs)


def track_routes(routes, start):
    stack = []
    next = start
    while next != 0:
        stack.append(next)
        next = routes[next]
    return stack[::-1]


routes, costs = dijkstra(start)
routes = track_routes(routes, end)

print(costs[end])
print(len(routes))
for route in routes:
    print(route, end=" ")
