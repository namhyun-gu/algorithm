from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [0] * len(nums)
        length = 0

        for num in nums:
            l, r = 0, length
            while l != r:
                m = (l + r) // 2
                if memo[m] < num:
                    l = m + 1
                else:
                    r = m
            memo[l] = num
            length = max(l + 1, length)
        return length


if __name__ == "__main__":
    sol = Solution()

    ret = sol.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18])
    print(ret)  # Expect 4

    ret = sol.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3])
    print(ret)  # Expect 4

    ret = sol.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7])
    print(ret)  # Expect 1
