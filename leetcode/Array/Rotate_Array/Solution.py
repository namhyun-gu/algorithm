from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            temp = nums[-1]
            nums.insert(0, temp)
            nums.pop()

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    sol = Solution()
    sol.rotate(arr, 3)
    print(arr)