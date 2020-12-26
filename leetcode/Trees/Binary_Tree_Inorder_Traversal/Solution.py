from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []

        ret = []
        stack = []

        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ret.append(cur.val)
            cur = cur.right
        return ret

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []

        ret = []
        stack = []

        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            ret.append(cur.val)
            cur = cur.left
        return ret

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []

        ret = []
        stack = [root]

        while stack:
            cur = stack.pop()
            ret.append(cur.val)

            if cur.right:
                stack.append(cur.right)

            if cur.left:
                stack.append(cur.left)
        return ret


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
    ret = sol.inorderTraversal(root)  # Expect [1, 3, 2]
    print(ret)

    root = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    ret = sol.inorderTraversal(root)  # Expect [2, 1, 3]
    print(ret)

    ret = sol.preorderTraversal(root)  # Expect [1, 2, 3]
    print(ret)

    ret = sol.postorderTraversal(root)  # Expect [3, 1, 2]
    print(ret)