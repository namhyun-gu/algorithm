data class TreeNode(var `val`: Int, var left: TreeNode? = null, var right: TreeNode? = null)

class Solution {
    fun sortedArrayToBST(nums: IntArray): TreeNode? {
        return toBST(nums, 0, nums.size - 1)
    }
    
    fun toBST(nums: IntArray, start: Int, end: Int): TreeNode? {
        if (start > end) {
            return null
        }
        
        val half = (start + end) / 2
        val node = TreeNode(nums[half])
        node.left = toBST(nums, start, half - 1)
        node.right = toBST(nums, half + 1, end)
        return node
    }
}

val sol = Solution()
val nums = intArrayOf(-10, -3, 0, 5, 9)
sol.sortedArrayToBST(nums)

val sol = Solution()
val nums = intArrayOf(1, 3)
sol.sortedArrayToBST(nums)


