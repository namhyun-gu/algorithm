# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from heapq import heappush, heappop
from collections import deque


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        ? 첫번째 풀이

        k번째로 작은 값을 찾기 위해서
        BFS를 통해 모든 노드를 순회하면서 Heap에 담고
        Heap에서 꺼내는 방식으로 문제를 풀었다.

        ? 풀이 확인

        풀이를 확인해보니,
        내가 풀이한 방법은 BST의 특징을 이용하지 않아 비효율적인 면이 있었다.

        BST의 가장 왼쪽은 가장 작은 값을 가지고 있기에
        가장 작은 위치로 이동을 하고
        해당 위치부터 중위순위로 k번째를 찾으면 해결할 수 있다.
        """
        stack = []
        while True:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(3, left=TreeNode(1, TreeNode(2)), right=TreeNode(4))
    ret = sol.kthSmallest(root, 1)
    print(ret)  # Expect 1

    root = TreeNode(
        5, left=TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), right=TreeNode(6)
    )
    ret = sol.kthSmallest(root, 3)
    print(ret)  # Expect 3
