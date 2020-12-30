#
# Fenwick Tree
#
# Referece : https://www.acmicpc.net/blog/view/21

N = 25


def sum(tree, i):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= i & -i
    return ans


def update(tree, i, diff):
    while i < len(tree):
        tree[i] += diff
        i += i & -i


nums = [i for i in range(N)]
tree = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    update(tree, i, nums[i - 1])

pass