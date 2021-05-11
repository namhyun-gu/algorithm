class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        if (s.length != t.length) {
            return false
        }

        var sMap = mutableMapOf<Char, Int>()
        val tMap = mutableMapOf<Char, Int>()

        for (c in s) {
            sMap[c] = sMap.getOrDefault(c, 0) + 1
        }
        for (c in t) {
            tMap[c] = tMap.getOrDefault(c, 0) + 1
        }

        for (key in sMap.keys) {
            if (!tMap.containsKey(key)) {
                return false
            }
            if (sMap[key] != tMap[key]) {
                return false
            }
        }
        return true
    }
}