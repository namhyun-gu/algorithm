class Solution {
    fun reverseString(s: CharArray) {
        for (idx in 0 until s.size / 2) {
            swap(s, idx, s.size - 1 - idx)
        }
    }

    fun swap(s: CharArray, a: Int, b: Int) {
        val temp = s[a]
        s[a] = s[b]
        s[b] = temp
    }
}

val sol = Solution()
val example1 = "hello".toCharArray()
sol.reverseString(example1)
println(example1)

val example2 = "Hannah".toCharArray()
sol.reverseString(example2)
println(example2)