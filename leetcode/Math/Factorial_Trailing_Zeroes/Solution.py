class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0

        factorial = 1
        for i in range(2, n + 1):
            factorial *= i

        revered_factorial = str(factorial)[::-1]
        cnt = 0
        for c in revered_factorial:
            if c == "0":
                cnt += 1
            else:
                break
        return cnt


if __name__ == "__main__":
    sol = Solution()

    ret = sol.trailingZeroes(3)
    print(ret)  # Expect 0

    ret = sol.trailingZeroes(5)
    print(ret)  # Expect 1

    ret = sol.trailingZeroes(0)
    print(ret)  # Expect 0
