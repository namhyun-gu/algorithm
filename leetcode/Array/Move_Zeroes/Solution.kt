class Solution {
    fun moveZeroes(nums: IntArray): Unit {
        var nonZero = 0
        for (i in nums.indices) {
            if (nums[i] != 0) {
                nums[nonZero] = nums[i]
                nonZero += 1
            }
        }
        
        for (i in nonZero until nums.size) {
            nums[i] = 0
        } 
    }
}

val sol = Solution()

val nums = intArrayOf(0, 1, 0, 3, 12)

sol.moveZeroes(nums)

nums.contentToString()

val sol = Solution()

val nums = intArrayOf(0)

sol.moveZeroes(nums)

nums.contentToString()


