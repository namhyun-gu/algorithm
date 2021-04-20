class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        return nums.toSet().size != nums.size
    }
}

val nums = intArrayOf(1, 2, 3, 1)
val ret = Solution().containsDuplicate(nums)
println(ret)
