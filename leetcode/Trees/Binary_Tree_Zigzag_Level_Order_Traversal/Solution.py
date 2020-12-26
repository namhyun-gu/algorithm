from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []

        ret = []
        queue = deque([(root, 0)])

        while queue:
            cur, depth = queue.popleft()

            if depth == len(ret):
                ret.append([cur.val])
            else:
                if depth % 2:
                    ret[depth].insert(0, cur.val)
                else:
                    ret[depth].append(cur.val)

            if cur.left:
                queue.append((cur.left, depth + 1))
            if cur.right:
                queue.append((cur.right, depth + 1))

        return ret


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(
        3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))
    )
    ret = sol.zigzagLevelOrder(root)
    print(ret)  # Expect [[3], [20, 9], [15, 7]]

    root = TreeNode(
        1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3, right=TreeNode(5))
    )
    ret = sol.zigzagLevelOrder(root)
    print(ret)  # Expect [[1],[3,2],[4,5]]
