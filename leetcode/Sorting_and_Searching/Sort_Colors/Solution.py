from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_dict = {0: 0, 1: 0, 2: 0}
        for num in nums:
            num_dict[num] += 1

        idx = 0
        for num in range(3):
            for n in range(num_dict[num]):
                nums[idx] = num
                idx += 1


if __name__ == "__main__":
    sol = Solution()

    nums = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums)
    print(nums)

    nums = [2, 0, 1]
    sol.sortColors(nums)
    print(nums)

    nums = [0]
    sol.sortColors(nums)
    print(nums)

    nums = [1]
    sol.sortColors(nums)
    print(nums)
