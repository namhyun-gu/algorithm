# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        root = preorder.pop(0)
        root_idx = inorder.index(root)

        left_inorder_tree = inorder[:root_idx]
        left_size = len(left_inorder_tree)
        left_preorder_tree = preorder[:left_size]

        right_inorder_tree = inorder[root_idx + 1 :]
        right_preorder_tree = preorder[left_size:]

        left = self.buildTree(left_preorder_tree, left_inorder_tree)
        right = self.buildTree(right_preorder_tree, right_inorder_tree)

        return TreeNode(root, left, right)


from collections import defaultdict


def print_tree(root: TreeNode):
    queue = [(root, 0)]
    tree_dict = defaultdict(list)
    tree_depth = 0
    while queue:
        cur, depth = queue.pop(0)
        tree_dict[depth].append(cur.val)
        tree_depth = depth

        if cur.left:
            queue.append((cur.left, depth + 1))
        if cur.right:
            queue.append((cur.right, depth + 1))

    for depth in range(tree_depth + 1):
        print(f"{depth}: {tree_dict[depth]}")


if __name__ == "__main__":
    sol = Solution()

    ret = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print_tree(ret)