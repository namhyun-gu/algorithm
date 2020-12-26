from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for idx in reversed(range(len(digits))):
            if digits[idx] == 10:
                if idx > 0:
                    digits[idx] = 0
                    digits[idx - 1] += 1
                else:
                    digits[idx] = 0
                    digits.insert(0, 1)
        return digits

if __name__ == "__main__":
    sol = Solution()
    ret = sol.plusOne([1, 2, 3])
    print(ret)

    ret = sol.plusOne([9, 9])
    print(ret)

    ret = sol.plusOne([0, 0])
    print(ret)  # Expected [0, 1]
