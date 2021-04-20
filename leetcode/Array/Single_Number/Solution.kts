class Solution {
    fun singleNumber(nums: IntArray): Int {
        val map = mutableMapOf<Int, Int>()

        for (num in nums) {
            map[num] = map.getOrDefault(num, 0) + 1
        }

        for (key in map.keys) {
            if (map[key] == 1) {
                return key
            }
        }
        return 0
    }
}

val nums = intArrayOf(1, 2, 3, 1)
val ret = Solution().singleNumber(nums)
println(ret)
