# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n

        min_version = n + 1
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                min_version = min(min_version, mid)
                right = mid - 1
            else:
                left = mid + 1
        return min_version