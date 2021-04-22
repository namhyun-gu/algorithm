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


def solution(n, costs):
    answer = 0

    costs.sort(key=lambda cost: cost[2])

    parent = [i for i in range(n)]

    for u, v, cost in costs:
        if find(parent, u) != find(parent, v):
            answer += cost
            union(parent, u, v)
    return answer