class Solution:
    def titleToNumber(self, s: str) -> int:
        reverse = map(ord, s[::-1])
        ret = 0
        for idx, n in enumerate(reverse):
            n -= 64
            ret += (26 ** idx) * n
        return ret


if __name__ == "__main__":
    sol = Solution()

    ret = sol.titleToNumber("A")
    print(ret)  # Expect 1

    ret = sol.titleToNumber("AB")
    print(ret)  # Expect 28

    ret = sol.titleToNumber("ZY")
    print(ret)  # Expect 701

    ret = sol.titleToNumber("AAA")
    print(ret)  # Expect 703