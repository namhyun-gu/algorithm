# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
이 문제를 처음 풀 때
알고 있던 BST의 정의는

노드 A에 대해 A의 왼쪽 노드는 A보다 작고
A의 오른쪽 노드는 A보다 크다

라는 것만 생각하고 한 노드만 비교했는데
왼쪽, 오른쪽 서브트리에 대해서 이 조건을 만족해야 된다는 것을
문제를 풀면서 알게 되었다.

탐색하며 비교할 때 BFS를 이용하여 탐색했는데
이 방식대로 비교를 한다면 전체 트리를 비교하고, 서브트리에 대해 비교하는 식의
비효율적인 방식 밖에 떠오르지 않았는데 솔루션을 확인하니

lower, upper를 각 노드들에 전달하며 비교를 하는데
이 변수들로 아래의 조건을 통해 유효한 BST임을 확인할 수 있다.

lower < node.val < upper

왼쪽 노드에 대해서는 (이전 lower < node < 현재 노드) 조건으로 비교하고,
오른쪽 노드에 대해서는 (현재 노드 < node < 이전 upper) 조건으로 비교한다.
"""


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._isValidBST(root)

    def _isValidBST(self, root, lower=None, upper=None):
        if root == None:
            return True

        val = root.val
        if lower != None and val <= lower:
            return False
        if upper != None and val >= upper:
            return False

        if not self._isValidBST(root.left, lower, val):
            return False
        if not self._isValidBST(root.right, val, upper):
            return False
        return True


if __name__ == "__main__":
    root = TreeNode(
        3, None, TreeNode(30, TreeNode(10, None, TreeNode(15, None, TreeNode(45))))
    )
    result = Solution().isValidBST(root)
    print(result)