# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def _sortedArrayToBST(self, nums, left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        left = self._sortedArrayToBST(nums, left, mid - 1)
        right = self._sortedArrayToBST(nums, mid + 1, right)
        return TreeNode(nums[mid], left, right)

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self._sortedArrayToBST(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    tree = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
    print(tree)