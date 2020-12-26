"""
이 문제는 '+'와 '-'을 사용하지 않고 값을 더하는 문제이다.
따라서 비트 연산을 통해 답을 구해야하는 데

자바로 구할 경우 다음과 같은 식을 통해 구할 수 있다고 한다.

class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int sum = a ^ b;
            int carry = (a & b) << 1;
            a = sum;
            b = carry;
        }
        return a;
    }
}

그러나 파이썬의 경우 다음과 같이 구현하면 답이 나오지 않는데
마스크 값을 사용해야만 해결할 수 있다고 하는데
비트 연산에 대해 공부해봐야 알 수 있을 것 같다.

Reference:
https://leetcode.com/problems/sum-of-two-integers/discuss/776952/Python-BEST-LeetCode-371-Explanation-for-Python
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b:
            sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = sum
            b = carry

        if (a >> 31) & 1:
            return ~(a ^ mask)

        return a


if __name__ == "__main__":
    sol = Solution()

    ret = sol.getSum(1, 2)
    print(ret)  # Expect 3

    ret = sol.getSum(-2, 3)
    print(ret)  # Expect 1
