class Solution {
    fun rotate(nums: IntArray, k: Int) {
        repeat(k) {
            val temp = nums[nums.size - 1]
            for (i in nums.size - 2 downTo 0) {
                nums[i + 1] = nums[i]
            }
            nums[0] = temp
        }
    }
}

val nums = intArrayOf(1, 2, 3, 4, 5, 6, 7)
val ret = Solution().rotate(nums, 3)
println(ret)
println(nums.contentToString())
