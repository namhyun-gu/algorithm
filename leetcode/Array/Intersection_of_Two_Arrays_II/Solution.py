from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        nums1.sort()
        nums2.sort()

        while nums1 and nums2:
            num1 = nums1[-1]
            num2 = nums2[-1]

            if num1 == num2:
                ret.append(num1)
                nums1.pop()
                nums2.pop()
            elif num1 < num2:
                nums2.pop()
            else:
                nums1.pop()

        return sorted(ret)


if __name__ == "__main__":
    sol = Solution()
    ret = sol.intersect([4, 9, 5], [9, 4, 9, 8, 4])
    print(ret)  # Expect [4, 9]

    ret = sol.intersect([1, 2], [1, 1])
    print(ret)  # Expect [1]

    ret = sol.intersect([1, 2, 2, 1], [2])
    print(ret)  # Expect [2]

    ret = sol.intersect([1, 2, 2, 1], [2, 2])
    print(ret)  # Expect [2, 2]
