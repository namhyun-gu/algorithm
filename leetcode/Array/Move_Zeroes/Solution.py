from typing import List

"""
이중 for 문을 이용하여 다음과 같이
swap 연산을 통해 작성을 했다. 통과는 했으나
솔루션을 확인해보니 효율적인 방법이 있었다.

def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == 0 and nums[j] != 0:
                    self.swap(nums, i, j)

def swap(self, arr: List[int], a: int, b: int):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


이 문제에서 0을 끝으로 옮긴다는 것은
0이 아닌 값을 앞으로 가져오는 것과 같다.
따라서, 0이 아닌 값을 앞으로 가져오고 0이 아닌 값 개수를 센 뒤 전체 배열에서 빼주면
0의 개수를 구할 수 있다. 끝에 이 개수만큼 0을 넣어주면 해결 할 수 있다.
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero] = nums[i]
                non_zero += 1

        for i in range(non_zero, len(nums)):
            nums[i] = 0


if __name__ == "__main__":
    sol = Solution()
    arr = [0, 1, 0, 3, 12]
    sol.moveZeroes(arr)
    print(arr)  # Expect [1, 3, 12, 0, 0]

    arr = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    sol.moveZeroes(arr)
    print(arr)  # Expect [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]
