class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ""
        for l in range(len(s)):
            for r in range(len(s), l, -1):
                if len(ret) >= r - l:
                    break
                elif s[l:r] == s[l:r][::-1]:
                    ret = s[l:r]
                    break
        return ret


if __name__ == "__main__":
    sol = Solution()

    ret = sol.longestPalindrome("babad")
    print(ret)  # Expect "bab"

    ret = sol.longestPalindrome("cbbd")
    print(ret)  # Expect "bb"

    ret = sol.longestPalindrome("a")
    print(ret)  # Expect "a"

    ret = sol.longestPalindrome("ac")
    print(ret)  # Expect "a"

    ret = sol.longestPalindrome("aacabdkacaa")
    print(ret)  # Expect "aca"
