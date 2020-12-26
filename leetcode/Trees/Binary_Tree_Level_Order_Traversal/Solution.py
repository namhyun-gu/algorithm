# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        traversal = []
        queue = deque([(root, 0)])

        if root == None:
            return []

        while queue:
            current, depth = queue.popleft()

            if depth == len(traversal):
                traversal.append([current.val])
            else:
                traversal[depth].append(current.val)

            if current.left != None:
                queue.append((current.left, depth + 1))
            if current.right != None:
                queue.append((current.right, depth + 1))
        return traversal


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    result = Solution().levelOrder(root)
    print(result)