# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, left: TreeNode, right: TreeNode) -> bool:
        if left != None and right != None:
            if left.val != right.val:
                return False

            ret = self._isSymmetric(left.left, right.right)
            if not ret:
                return False

            ret = self._isSymmetric(left.right, right.left)
            if not ret:
                return False

            return True
        elif left == None and right == None:
            return True
        return False


if __name__ == "__main__":
    sol = Solution()

    example1 = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
        right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)),
    )
    print(sol.isSymmetric(example1))  # Expect True

    example2 = TreeNode(
        1, left=TreeNode(2, right=TreeNode(3)), right=TreeNode(2, right=TreeNode(3))
    )
    print(sol.isSymmetric(example2))  # Expect False
