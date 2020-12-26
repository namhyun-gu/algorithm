from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict = dict()
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        for num in num_dict.keys():
            if num_dict[num] == 1:
                return num
        return 0
