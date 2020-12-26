from typing import List

import random


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original_nums = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.original_nums
        self.original_nums = list(self.original_nums)
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        temp = list(self.nums)
        for idx in range(len(self.nums)):
            rand = random.randrange(len(temp))
            self.nums[idx] = temp.pop(rand)
        return self.nums


# Your Solution object will be instantiated and called as such:
if __name__ == "__main__":
    nums = [1, 2, 3]
    obj = Solution(nums)
    param_1 = obj.reset()
    param_2 = obj.shuffle()
    print(param_1, param_2)