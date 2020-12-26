class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        for i in range(len(nums)):
            if prev == None or nums[0] != prev:
                nums.append(nums[0])
                prev = nums[0]
            nums.pop(0)
        return len(nums)