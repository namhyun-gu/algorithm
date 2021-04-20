class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        if (nums.isEmpty()) {
            return 0
        }

        var idx = 0
        var temp = nums[0]
        for (i in 1 until nums.size) {
            if (nums[i] != temp) {
                temp = nums[i]
                nums[++idx] = nums[i]
            }
        }
        val size = idx + 1
        for (i in size until nums.size) {
            nums[i] = 0
        }
        return size
    }
}

val nums = intArrayOf(1, 1, 2)
val ret = Solution().removeDuplicates(nums)
println(ret)
println(nums.contentToString())
