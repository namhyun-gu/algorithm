from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        prev = None
        pivot = None
        for idx, num in enumerate(nums):
            if prev and prev > num:
                pivot = idx
                break
            else:
                prev = num

        if target >= nums[0]:
            return self._search(nums[:pivot], target)
        else:
            ret = self._search(nums[pivot:], target)
            return ret + pivot if ret > -1 else ret

    def _search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    sol = Solution()

    ret = sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
    print(ret)  # Expected 4

    ret = sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3)
    print(ret)  # Expected -1

    ret = sol.search(nums=[1], target=0)
    print(ret)  # Expected -1
