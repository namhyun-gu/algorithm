import kotlin.math.min

class Solution {
    fun firstUniqChar(s: String): Int {
        val count = mutableMapOf<Char, Int>()
        val index = mutableMapOf<Char, Int>()
        for (idx in s.indices) {
            val c = s[idx]
            count[c] = count.getOrDefault(c, 0) + 1
            index[c] = idx
        }

        var minIdx = s.length
        for (key in count.keys) {
            if (count[key] == 1) {
                minIdx = min(minIdx, index[key]!!)
            }
        }
        return if (minIdx == s.length) {
            -1
        } else {
            minIdx
        }
    }
}