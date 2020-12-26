from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        diff = set(range(n + 1)).difference(set(nums))
        return list(diff)[0]


if __name__ == "__main__":
    sol = Solution()

    print(sol.missingNumber([3, 0, 1]))  # Expect 2
    print(sol.missingNumber([0, 1]))  # Expect 2
    print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Expect 8
    print(sol.missingNumber([0]))  # Expect 1
