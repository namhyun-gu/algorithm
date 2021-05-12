class Solution {
    fun intersect(nums1: IntArray, nums2: IntArray): IntArray {
        nums1.sort()
        nums2.sort()
        
        return if (nums1.size < nums2.size) {
            innerIntersect(nums1, nums2)
        } else {
            innerIntersect(nums2, nums1)
        }
    }
    
    fun innerIntersect(nums1: IntArray, nums2: IntArray): IntArray {
        val intersected = mutableListOf<Int>()
        var idx1 = 0
        var idx2 = 0
        
        while (idx1 < nums1.size && idx2 < nums2.size) {
            if (nums1[idx1] < nums2[idx2]) {
                idx1++
            } else if (nums1[idx1] > nums2[idx2]) {
                idx2++
            } else {
                intersected.add(nums1[idx1])
                idx1++
                idx2++
            }
        }
        return intersected.toIntArray()
    }
}

val sol = Solution()

val nums1 = intArrayOf(1, 2, 2, 1)
val nums2 = intArrayOf(2, 2)

sol.intersect(nums1, nums2).contentToString()

val sol = Solution()

val nums1 = intArrayOf(4, 9, 5)
val nums2 = intArrayOf(9, 4, 9, 8, 4)

sol.intersect(nums1, nums2).contentToString()

val sol = Solution()

val nums1 = intArrayOf(4, 7, 9, 7, 6, 7)
val nums2 = intArrayOf(5, 0, 0, 6, 1, 6, 2, 2, 4)

sol.intersect(nums1, nums2).contentToString()


