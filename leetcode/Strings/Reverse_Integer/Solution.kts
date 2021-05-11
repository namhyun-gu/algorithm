import kotlin.math.abs

class Solution {
    fun reverse(x: Int): Int {
        return try {
            val negative = x < 0
            var result = abs(x).toString().reversed().toInt()
            if (negative) {
                result *= -1
            }
            result
        } catch (e: NumberFormatException) {
            0
        }
    }
}

val sol = Solution()

val example1 = 123
println(sol.reverse(example1))

val example2 = -123
println(sol.reverse(example2))

val example3 = 120
println(sol.reverse(example3))

val example4 = 0
println(sol.reverse(example4))
