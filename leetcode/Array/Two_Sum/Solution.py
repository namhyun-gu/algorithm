from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            try:
                target_idx = nums.index(target - num)
                if target_idx >= 0 and target_idx != idx:
                    return [idx, target_idx]
            except ValueError:
                continue
        return []