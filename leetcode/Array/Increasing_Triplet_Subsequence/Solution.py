from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = float("inf"), float("inf")

        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()

    ret = sol.increasingTriplet([1, 2, 3, 4, 5])
    assert ret == True

    ret = sol.increasingTriplet([5, 4, 3, 2, 1])
    assert ret == False

    ret = sol.increasingTriplet([2, 1, 5, 0, 4, 6])
    assert ret == True

    ret = sol.increasingTriplet([5, 1, 5, 5, 2, 5, 4])
    assert ret == True