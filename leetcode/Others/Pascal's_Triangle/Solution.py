from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row in range(numRows):
            line = [0] * (row + 1)
            for col in range(row + 1):
                if col == 0 or col == row:
                    line[col] = 1
                else:
                    if row > 1:
                        line[col] = (
                            triangle[row - 1][col - 1] + triangle[row - 1][col]
                        )
            triangle.append(line)
        return triangle


def printTriangle(triangle):
    for row in range(len(triangle)):
        print(triangle[row])


if __name__ == "__main__":
    sol = Solution()
    triangle = sol.generate(5)
    printTriangle(triangle)
