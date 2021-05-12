class Solution {
    fun plusOne(digits: IntArray): IntArray {
        var carry = false
        digits[digits.size - 1] += 1
        for (idx in digits.size - 1 downTo 0) {
            if (digits[idx] == 10) {
                digits[idx] = 0
                if (idx > 0) {
                    digits[idx - 1] += 1
                } else {
                    carry = true
                }
            }
        }
        
        if (carry) {
            return intArrayOf(1, *digits)
        }
        return digits
        
    }
}

val sol = Solution()

val digits = intArrayOf(1, 2, 2, 1)

sol.plusOne(digits).contentToString()

val sol = Solution()

val digits = intArrayOf(9, 9)

sol.plusOne(digits).contentToString()

val sol = Solution()

val digits = intArrayOf(0)

sol.plusOne(digits).contentToString()

val sol = Solution()

val digits = intArrayOf(9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

sol.plusOne(digits).contentToString()


