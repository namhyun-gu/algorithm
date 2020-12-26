from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [nums[i] for i in range(len(nums))]

        for idx in range(len(nums)):
            if idx > 2:
                dp[idx] = max(dp[idx] + dp[idx - 2], dp[idx] + dp[idx - 3])
            elif idx > 1:
                dp[idx] = dp[idx] + dp[idx - 2]

        if len(dp) > 0:
            return max(dp)
        else:
            return 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1, 2, 3, 1]))  # Expect 4
    print(sol.rob([2, 7, 9, 3, 1]))  # Expect 12
