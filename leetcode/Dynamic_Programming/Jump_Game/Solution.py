from typing import List

"""
문제를 처음 접근할 때,

nums 크기만큼의 배열 jump을 -1로 초기화하고,

jump[i] = i로 올 수 있는 점프 길이

for i in range(1, len(nums)):
    for j in range(i):
        # ...

위 방식과 같이 이중 for문을 이용하여 값을 구하고,
jump[-1]의 값이 -1이 아닌지를 판별하였는데

이 방식대로 하게 되면 Time Limit Exceeded 가 발생한다.

솔루션을 확인해보니,
O(n)으로 구할 수 있는 그리디한 방법이 있었다.

무조건 0부터 시작하여 끝을 구한다는 생각이 있었는데,
이는 반대로 시작하여,
해당 자리와 점프 가능한 길이를 더했을 때, 현 위치에 올 수 있다면
위치를 업데이트하는 식으로 구하고

최종적으로 위치가 0에 도달하는 지를 확인하여 구한다.
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        position = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] >= position:
                position = i
        return position == 0


if __name__ == "__main__":
    sol = Solution()

    ret = sol.canJump([2, 3, 1, 1, 4])
    print(ret)

    ret = sol.canJump([3, 2, 1, 0, 4])
    print(ret)