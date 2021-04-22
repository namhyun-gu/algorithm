# Ref: https://blog.naver.com/ndb796/221230994142

# 부모 노드를 가져오는 과정
def find(parent, x):
    if x == parent[x]:
        return x

    # x와 x의 부모가 같지 않다면, x의 부모를 찾는다.
    parent[x] = find(parent, parent[x])
    return parent[x]


# X, Y의 부모 노드를 병합
def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    # 더 작은 부모 노드의 숫자로 병합
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


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

n = 7
parent = [i for i in range(n)]

# 간선의 비용으로 오름차순 정렬
edges.sort(key=lambda edge: edge[2])

sum = 0
for u, v, w in edges:
    u -= 1
    v -= 1

    # u와 v의 부모가 같지 않은 경우,
    # 즉, 사이클이 발생하지 않을 때 이 간선을 선택함
    if find(parent, u) != find(parent, v):
        sum += w
        union(parent, u, v)

print(sum)