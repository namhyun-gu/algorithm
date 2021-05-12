class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        for (i in 0 until nums.size) {
            for (j in i + 1 until nums.size) {
                if (target - nums[i] == nums[j]) {
                    return intArrayOf(i, j)
                }
            }
        }
        return intArrayOf(0, 1)
    }
}

val sol = Solution()

val nums = intArrayOf(2, 7, 11, 15)
val target = 9

sol.twoSum(nums, target).contentToString()

val sol = Solution()

val nums = intArrayOf(3, 2, 4)
val target = 6

sol.twoSum(nums, target).contentToString()

val sol = Solution()

val nums = intArrayOf(3, 3)
val target = 6

sol.twoSum(nums, target).contentToString()


