class Solution:
    def reverse(self, x: int) -> int:
        limit = 2_147_483_648
        
        a = 1
        n = x
        if x < 0:
            n *= -1
            a = -1
        n = int(str(n)[::-1])

        if n < limit:
            return n * a
        else:
            return 0