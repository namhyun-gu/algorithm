class Solution:
    def reverseBits(self, n: int) -> int:
        new_n = 0
        for i in reversed(range(32)):
            new_n += (n & 1) << i
            n = n >> 1
        return new_n