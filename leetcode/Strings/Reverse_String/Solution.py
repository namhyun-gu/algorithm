from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for idx in range(len(s) // 2):
            temp = s[idx]
            s[idx] = s[-(idx + 1)]
            s[-(idx + 1)] = temp

if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    print(s)