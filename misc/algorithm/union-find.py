"""
Union-Find

Ref: https://ko.wikipedia.org/wiki/서로소_집합_자료_구조
"""
MAX = 5
graph = [[1, 2], [2, 3], [4, 5]]

parent = [i for i in range(MAX + 1)]


def find(x):
    if x == parent[x]:
        return x
    return find(parent[x])


def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return

    parent[y_root] = x_root


for line in graph:
    root, child = line
    union(root, child)

"""
Output: [0, 1, 1, 1, 4, 4]

> 2는 1과 연결, 3은 1과 연결, 5는 4와 연결
"""
print(parent)
