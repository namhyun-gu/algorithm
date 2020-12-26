class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Sqrt를 구하는 과정은 1부터 x의 절반 값에서
        제곱한 값이 x와 같은 값을 찾는 과정이다.

        1부터 절반까지 확인하는 과정은 단순하지만 시간초과가 발생하므로
        Binary Search를 통해 맞는 값을 찾도록 변경하면 해결할 수 있다.

        left는 1로, right는 x의 절반 + 1로 지정했는데
        right의 값에 1을 더한 것은 나눴을 때 (eg. sqrt(4) = 2)
        정답으로 값이 딱 떨어지는 경우가 있기때문에 그보다 큰 값을 지정한다.
        """
        if x == 0 or x == 1:
            return x
        if x == 2:
            return 1

        l, r = 1, x // 2 + 1
        ret = 0
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ret = mid
                l = mid + 1
            else:
                r = mid - 1
        return ret


if __name__ == "__main__":
    sol = Solution()

    ret = sol.mySqrt(4)
    print(ret)  # Expect 2

    ret = sol.mySqrt(8)
    print(ret)  # Expect 2
