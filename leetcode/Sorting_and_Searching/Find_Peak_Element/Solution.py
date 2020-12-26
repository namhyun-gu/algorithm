from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == "__main__":
    sol = Solution()

    ret = sol.findPeakElement([1, 2, 3, 1])
    print(ret)  # Expect 2

    ret = sol.findPeakElement([1, 2, 1, 3, 5, 6, 4])
    print(ret)  # Expect 5
