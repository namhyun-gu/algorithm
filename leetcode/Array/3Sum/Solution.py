from typing import List

"""
이 문제를 처음 풀 때
x + y + z = 0 인 경우를 구하기 위해

for x in 0..nums.size:
    for y in x + 1..nums.size:
        for z in y + 1..nums.size:
            ...

3중 포문의 방법으로 문제를 해결하려 했다.
제출하니 시간초과가 발생이 되어 해결방법이 떠오르지 않아 솔루션을 검색했다.

솔루션에서는,
이분탐색을 이용하기 위해 배열을 정렬하고,
x의 값을 고정하고 이분탐색을 통해 y와 z를 각각 left, right로 탐색한다.
합이 0이 될 때 결과값에 배열을 더해주는 방식으로 해결한다.

합이 0이 될 때 값 하나만 더해주는 것이 아니라
left, right 값을 조정해주는 데 이유는 다른 y, z로 0이 될 수 있기 때문이다.

이를 조정할 때 중복된 값으로 계산하지 않도록
중복된 값이 없을때까지 반복하여 각각 더하고 빼준다.
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()

        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                picks = [nums[idx], nums[left], nums[right]]
                num_sum = sum(picks)
                if num_sum < 0:
                    left += 1
                elif num_sum > 0:
                    right -= 1
                else:
                    ret.append(picks)
                    while left < len(nums) - 1 and nums[left] == nums[left + 1]:
                        left += 1
                    while right > 0 and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ret


if __name__ == "__main__":
    sol = Solution()

    ret = sol.threeSum([-1, 0, 1, 2, -1, -4])
    print(ret)  # Expect [[-1,-1,2],[-1,0,1]]

    ret = sol.threeSum([])
    print(ret)  # Expect []

    ret = sol.threeSum([0])
    print(ret)  # Expect []