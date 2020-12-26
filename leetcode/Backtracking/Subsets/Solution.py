from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = list()
        n = len(nums)

        def _subsets(picks: List[int] = [], first: int = 0):
            ret.append(picks[:])

            for idx in range(first, n):
                picks.append(nums[idx])
                _subsets(picks, idx + 1) 
                picks.pop()

        _subsets()
        return ret


if __name__ == "__main__":
    sol = Solution()

    ret = sol.subsets([1, 2, 3])
    print(ret)  # Expect [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    ret = sol.subsets([0])
    print(ret)  # Expect [[],[0]]

    ret = sol.subsets([1, 2, 3, 4, 5, 6, 7, 8, 10, 0])
    print(ret)
