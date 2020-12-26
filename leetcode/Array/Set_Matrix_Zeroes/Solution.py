from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows or j in cols:
                    matrix[i][j] = 0


if __name__ == "__main__":
    sol = Solution()

    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    ret = sol.setZeroes(matrix)
    print(matrix)  # Expected [[1,0,1],[0,0,0],[1,0,1]]

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    ret = sol.setZeroes(matrix)
    print(matrix)  # Expected [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
