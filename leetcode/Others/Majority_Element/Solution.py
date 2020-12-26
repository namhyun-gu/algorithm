from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """ Boyer-Moore Voting Algorithm """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate


if __name__ == "__main__":
    sol = Solution()

    ret = sol.majorityElement([3, 2, 3])
    assert ret == 3

    ret = sol.majorityElement([2, 2, 1, 1, 1, 2, 2])
    assert ret == 2