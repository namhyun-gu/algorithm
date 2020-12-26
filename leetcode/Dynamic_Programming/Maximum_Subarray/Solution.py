from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = [nums[i] for i in range(len(nums))]

        for idx in range(len(nums)):
            if idx > 0:
                sum[idx] = max(sum[idx], sum[idx] + sum[idx - 1])

        return max(sum)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(sol.maxSubArray([1]))
    print(sol.maxSubArray([0]))
    print(sol.maxSubArray([-1]))
    print(sol.maxSubArray([-2147483647]))