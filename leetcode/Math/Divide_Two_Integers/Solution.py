class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN, MAX = -(2 ** 31), 2 ** 31 - 1

        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor, ret = abs(dividend), abs(divisor), 0

        while dividend >= divisor:
            temp, n = divisor, 1
            while dividend >= temp:
                dividend -= temp
                ret += n
                n <<= 1
                temp <<= 1

        if not positive:
            ret = -ret
            return max(ret, MIN)
        else:
            return min(ret, MAX)


if __name__ == "__main__":
    sol = Solution()

    ret = sol.divide(dividend=10, divisor=3)
    print(ret)  # Expect 3

    ret = sol.divide(dividend=7, divisor=-3)
    print(ret)  # Expect -2

    ret = sol.divide(dividend=0, divisor=1)
    print(ret)  # Expect 0

    ret = sol.divide(dividend=1, divisor=1)
    print(ret)  # Expect 1

    ret = sol.divide(dividend=-2147483648, divisor=-1)
    print(ret)  # Expect 2147483647

    ret = sol.divide(dividend=-2147483648, divisor=1)
    print(ret)  # Expect -2147483648