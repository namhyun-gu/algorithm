class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = list(filter(lambda c: c.isalnum(), s.lower()))
        for idx in range(len(filtered) // 2):
            if filtered[idx] != filtered[-(idx + 1)]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    ans = sol.isPalindrome("A man, a plan, a canal: Panama")
    print(ans)