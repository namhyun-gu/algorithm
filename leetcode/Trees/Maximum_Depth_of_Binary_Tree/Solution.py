# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        queue = deque([(root, 1)])
        max_depth = 0

        while queue:
            current, depth = queue.popleft()
            max_depth = max(max_depth, depth)

            if current.left != None:
                queue.append((current.left, depth + 1))
            if current.right != None:
                queue.append((current.right, depth + 1))

        return max_depth