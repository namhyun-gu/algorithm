from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 0:
            return

        nums1_idx = 0
        nums2_idx = 0
        temp = [nums1[i] for i in range(m)]

        idx = 0
        while nums1_idx < m and nums2_idx < n:
            if temp[nums1_idx] <= nums2[nums2_idx]:
                nums1[idx] = temp[nums1_idx]
                nums1_idx += 1
            elif temp[nums1_idx] > nums2[nums2_idx]:
                nums1[idx] = nums2[nums2_idx]
                nums2_idx += 1
            idx += 1

        while nums1_idx < m:
            nums1[idx] = temp[nums1_idx]
            nums1_idx += 1
            idx += 1

        while nums2_idx < n:
            nums1[idx] = nums2[nums2_idx]
            nums2_idx += 1
            idx += 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    Solution().merge(nums1, 3, [2, 5, 6], 3)
    print(nums1)
