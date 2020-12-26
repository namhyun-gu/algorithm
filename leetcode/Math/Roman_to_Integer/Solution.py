class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        prev = None
        for c in reversed(s):
            if (
                (c == "I" and prev in ["V", "X"])
                or (c == "X" and prev in ["L", "C"])
                or (c == "C" and prev in ["D", "M"])
            ):
                result -= roman_dict[c]
            else:
                result += roman_dict[c]
            prev = c
        return result