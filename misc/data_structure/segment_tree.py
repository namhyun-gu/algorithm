#
# Segment Tree
#
# Referece : https://www.acmicpc.net/blog/view/9

N = 25


def init(list, tree, node, start, end):
    if start == end:
        tree[node] = list[start]
    else:
        l = init(list, tree, node * 2, start, (start + end) // 2)
        r = init(list, tree, node * 2 + 1, (start + end) // 2 + 1, end)
        tree[node] = l + r
    return tree[node]


def sum(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]

    l = sum(tree, node * 2, start, (start + end) // 2, left, right)
    r = sum(tree, node * 2 + 1, (start + end) // 2 + 1, end, left, right)
    return l + r


def update(tree, node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] = tree[node] + diff
    if start != end:
        update(tree, node * 2, start, (start + end) // 2, index, diff)
        update(tree, node * 2 + 1, (start + end) // 2 + 1, end, index, diff)


from math import ceil, log2

nums = [i for i in range(N)]

# H = lgN (올림)
# 트리를 만드는데 필요한 배열의 크기 : 2^(H+1) - 1
h = ceil(log2(N))
tree = [0 for i in range(1 << (h + 1))]

init(nums, tree, 1, 0, N - 1)