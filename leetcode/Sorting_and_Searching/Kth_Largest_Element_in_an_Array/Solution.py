from typing import List


from heapq import heapify, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda i: (-i, i), nums))
        heapify(nums)
        for _ in range(k - 1):
            heappop(nums)
        return heappop(nums)[1]


if __name__ == "__main__":
    sol = Solution()

    ret = sol.findKthLargest([3, 2, 1, 5, 6, 4], 2)
    print(ret)  # Expect 5

    ret = sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    print(ret)  # Expect 4
