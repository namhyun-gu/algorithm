from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def _permute(nums: List[int], picks: List[int] = [], depth: int = 0):
            if depth == len(nums):
                ret.append(picks)
                return

            for num in nums:
                if num not in picks:
                    picks.append(num)
                    _permute(nums, list(picks), depth + 1)
                    picks.remove(num)

        _permute(nums)
        return ret


if __name__ == "__main__":
    sol = Solution()

    ret = sol.permute([1, 2, 3])
    print(ret)  # Expect [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    ret = sol.permute([0, 1])
    print(ret)  # Expect [[0,1],[1,0]]

    ret = sol.permute([1])
    print(ret)  # Expect [[1]]
