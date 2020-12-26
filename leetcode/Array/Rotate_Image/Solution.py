from typing import List

"""
행렬을 시계 방향으로 90도 회전하면 되는 문제이다.

어떻게 회전을 해야할지 감이 오지 않아 솔루션을 확인하였더니

행렬을 Transpose 한 뒤, 각 행을 Reverse 하면 회전행렬을 얻을 수 있다고 한다.

솔루션 내 토론 내용에 따르면,
파이썬이 제공하는 Reverse 함수로 행렬 전체를 Reverse 한 뒤, Transpose 해도 얻을 수 있다고 한다.

* Transpose 할 때 Swap 연산이 필요한데 이는 Tuple과, Destructuring를 이용하면 간결하게 작성할 수 있다.
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)

        matrix.reverse()
        # Transpose
        for i in range(size):
            for j in range(i, size):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        # Reverse
        # for i in range(size):
        #     matrix[i].reverse()


if __name__ == "__main__":
    sol = Solution()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(matrix)
    print(matrix)

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol.rotate(matrix)
    print(matrix)
