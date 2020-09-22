from .. import util

example = """
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
"""
util.setinput(example)

import sys
input = sys.stdin.readline

N = int(input())
tree = {}
for _ in range(N):
    cur, left, right = input().split()
    tree[cur] = (left, right)


def preorder(tree, root):
    left, right = tree[root]
    print(root, end="")
    if left != '.':
        preorder(tree, left)
    if right != '.':
        preorder(tree, right)


def inorder(tree, root):
    left, right = tree[root]
    if left != '.':
        inorder(tree, left)
    print(root, end="")
    if right != '.':
        inorder(tree, right)


def postorder(tree, root):
    left, right = tree[root]
    if left != '.':
        postorder(tree, left)
    if right != '.':
        postorder(tree, right)
    print(root, end="")


preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree, 'A')
