from typing import List


class Solution:
    def __init__(self) -> None:
        self.ret = []

    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if len(digits) == 0:
            return self.ret

        letters = list(map(lambda it: digit_to_letter[it], digits))
        self._letterCombinations(letters)
        return self.ret

    def _letterCombinations(self, letters: List[str], picks: str = "", length: int = 0):
        if length == len(letters):
            self.ret.append(picks)
            return

        for current in letters[length]:
            self._letterCombinations(letters, picks + current, length + 1)


if __name__ == "__main__":
    sol = Solution()

    ret = sol.letterCombinations("23")
    print(ret)

    ret = sol.letterCombinations("")
    print(ret)

    ret = sol.letterCombinations("2")
    print(ret)