"""
Hamming Distance

1 : 0001
4 : 0100

1^4 = 0101

1) 0b101 : 0b101 & 1 = 1
2) 0b10 : 0b10 & 1 = 0
3) 0b1 : 0b1 & 1 = 1

dist = 2
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        val = x ^ y

        while val > 0:
            if val & 1:
                dist += 1
            val = val >> 1
        return dist


if __name__ == "__main__":
    sol = Solution()
    sol.hammingDistance(1, 4)