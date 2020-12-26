from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False

        rows, cols = len(board), len(board[0])

        def match(row, col, index):
            if self.found:
                return

            if index == len(word):
                self.found = True
                return

            if row not in range(rows) or col not in range(cols):
                return

            if board[row][col] != word[index]:
                return

            temp = board[row][col]
            board[row][col] = "#"

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                match(row + dr, col + dc, index + 1)

            board[row][col] = temp

        for row in range(rows):
            for col in range(cols):
                if self.found:
                    return True
                match(row, col, 0)
        return self.found


if __name__ == "__main__":
    sol = Solution()

    ret = sol.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED",
    )
    print(ret)  # Expected true

    ret = sol.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="SEE",
    )
    print(ret)  # Expected true

    ret = sol.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCB",
    )
    print(ret)  # Expected false

    ret = sol.exist(board=[["a", "b"], ["c", "d"]], word="cdba")
    print(ret)  # Expected True

    ret = sol.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
        word="ABCESEEEFS",
    )
    print(ret)  # Expected True
