from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board[0])

        for i in range(size):
            row_set = set()
            col_set = set()
            for j in range(size):
                row = board[i][j]
                col = board[j][i]
                if row != ".":
                    if row not in row_set:
                        row_set.add(row)
                    else:
                        return False
                
                if col != ".":
                    if col not in col_set:
                        col_set.add(col)
                    else:
                        return False

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                ret = self._isValidSudokuBox(board, j, i)
                if not ret:
                    return False
        return True

    def _isValidSudokuBox(self, board: List[List[str]], row: int, col: int) -> bool:
        box_set = set()
        for i in range(3):
            for j in range(3):
                it = board[col + i][row + j]
                if it != ".":
                    if it not in box_set:
                        box_set.add(it)
                    else:
                        return False
        return True


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(sol.isValidSudoku(board))  # Expect True

    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(sol.isValidSudoku(board))  # Expect False
