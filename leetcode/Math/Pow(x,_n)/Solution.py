class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self._pow(x, -n)
        else:
            return self._pow(x, n)

    def _pow(self, x: float, n: int) -> float:
        """
        pow(x, n) =
            (n = 0) 1
            (n이 홀수) pow(x, n / 2)^2 * x
            (n이 짝수) pow(x, n / 2)^2

        Ref: https://onsil-thegreenhouse.github.io/programming/problem/2018/03/29/problem_math_power/
        """
        if n == 0:
            return 1
        else:
            temp = self._pow(x, n // 2)
            if n % 2:
                return temp * temp * x
            else:
                return temp * temp


if __name__ == "__main__":
    sol = Solution()

    ret = sol.myPow(x=2.00000, n=10)
    print(ret)  # Expect 1024.00000

    ret = sol.myPow(x=2.10000, n=3)
    print(ret)  # Expect 9.26100

    ret = sol.myPow(x=2.00000, n=-2)
    print(ret)  # Expect 0.25000
