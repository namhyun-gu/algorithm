from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        find = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                find = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if find == -1:
            return [-1, -1]

        l, r = find, find
        while l >= 0 and nums[l] == target:
            l -= 1
        while r < len(nums) and nums[r] == target:
            r += 1
        l += 1
        r -= 1
        return [l, r]


if __name__ == "__main__":
    sol = Solution()

    ret = sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8)
    print(ret)  # Expect [3, 4]

    ret = sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6)
    print(ret)  # Expect [-1, -1]

    ret = sol.searchRange(nums=[], target=0)
    print(ret)  # Expect [-1, -1]

    ret = sol.searchRange(nums=[1], target=1)
    print(ret)  # Expect [0, 0]
