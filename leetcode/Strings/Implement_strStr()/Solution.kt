class Solution {
    fun strStr(haystack: String, needle: String): Int {
        if (needle.isEmpty()) {
            return 0
        }
        
        for (i in 0 until haystack.length) {
            if (i + needle.length > haystack.length) {
                break
            }
            
            var find = false
            for (j in 0 until needle.length) {
                if (haystack[i + j] != needle[j]) {
                    break
                }
                if (j == needle.length - 1) {
                    find = true
                }
            }
            if (find) {
                return i
            }
        }
        return -1
    }
}

val sol = Solution()
val haystack = "hello"
val needle = "ll"

sol.strStr(haystack, needle)

val sol = Solution()
val haystack = "aaaaa"
val needle = "bba"

sol.strStr(haystack, needle)

val sol = Solution()
val haystack = ""
val needle = ""

sol.strStr(haystack, needle)

val sol = Solution()
val haystack = ""
val needle = "a"

sol.strStr(haystack, needle)

val sol = Solution()
val haystack = "a"
val needle = "a"

sol.strStr(haystack, needle)

val sol = Solution()
val haystack = "mississippi"
val needle = "mississippi"

sol.strStr(haystack, needle)


