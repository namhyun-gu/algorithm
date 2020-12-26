from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [0] * len(nums)
        ret[0] = 1

        # i번째에 i번째 앞까지의 곱을 구함 (왼쪽)
        # [1, 1, 2, 6]
        for i in range(1, len(nums)):
            ret[i] = ret[i - 1] * nums[i - 1]

        # 뒤에서부터 i번째 뒤까지의 곱을 구하고 i번째에 곱함 (오른쪽)
        # [1, 1, 2, (6)] (R = 1)
        # [1, 1, (8), 6] (R = 4)
        # [1, (12), 8, 6] (R = 12)
        # [(24), 12, 8, 6] (R = 24)
        R = 1
        for i in reversed(range(len(nums))):
            ret[i] = ret[i] * R
            R *= nums[i]
        return ret


if __name__ == "__main__":
    sol = Solution()

    ret = sol.productExceptSelf([1, 2, 3, 4])
    print(ret)  # Expected [24, 12, 8, 6]
