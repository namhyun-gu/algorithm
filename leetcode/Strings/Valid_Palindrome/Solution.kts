class Solution {
    fun isPalindrome(s: String): Boolean {
        val builder = StringBuilder()
        for (c in s) {
            if (c in 'a'..'z' || c in '0'..'9') {
                builder.append(c)
            } else if (c in 'A'..'Z') {
                builder.append(c + ('a' - 'A'))
            }
        }
        val str = builder.toString()
        return str == str.reversed()
    }
}