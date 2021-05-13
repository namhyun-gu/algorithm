class Solution {
    fun countAndSay(n: Int): String {
        if (n == 1) {
            return "1"
        }
        val count = countAndSay(n - 1)
        var temp = count[0]
        
        var builder = StringBuilder()
        var cnt = 1
        for (idx in 1 until count.length) {
            if (count[idx] != temp) {
                builder.append("${cnt}${temp}")
                temp = count[idx]
                cnt = 1
            } else {
                cnt += 1
            }
        }
        builder.append("${cnt}${temp}")
        return builder.toString()
    }
}

val sol = Solution()
val n = 1

sol.countAndSay(n)

val sol = Solution()
val n = 4

sol.countAndSay(n)

val sol = Solution()
val n = 5

sol.countAndSay(n)

val sol = Solution()
val n = 6

sol.countAndSay(n)


