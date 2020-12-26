from typing import List

from collections import deque


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        queue = deque([(0, 0)])
        visit = set()
        while queue:
            r, c = queue.popleft()
            if (r, c) in visit:
                continue

            visit.add((r, c))

            if r not in range(rows) or c not in range(cols):
                continue

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                queue.append((r + 1, c))
                queue.append((r, c + 1))
            elif matrix[r][c] > target:
                queue.append((r - 1, c))
                queue.append((r, c - 1))
        return False


if __name__ == "__main__":
    sol = Solution()

    ret = sol.searchMatrix(
        matrix=[
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        target=5,
    )
    print(ret)  # Expected True
    ret = sol.searchMatrix(
        matrix=[
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        target=20,
    )
    print(ret)  # Expected False
