# region Input redirection
import io
import sys

example = """
5
-1 0 0 1 1
0
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import collections


def calculate_leaf(tree, node, ignore):
    sum = 0
    for next in tree[node]:
        if next == ignore:
            continue

        sum += calculate_leaf(tree, next, ignore)

    if not sum:
        return 1
    return sum


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())

    tree = collections.defaultdict(list)
    root = None

    for node, parent in enumerate(map(int, input().split())):
        if parent == -1:
            root = node
        else:
            tree[parent].append(node)

    target = int(input())
    
    if root != target:
        answer = calculate_leaf(tree, root, target)
    else:
        answer = 0
    print(answer)