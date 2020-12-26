class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [True for _ in range(n)]
        if n > 1:
            sieve[1] = False

        m = int(n ** 0.5)
        for i in range(2, m + 1):
            if sieve[i]:
                for j in range(i + i, n, i):
                    sieve[j] = False

        count = 0
        for i in range(1, n):
            if sieve[i]:
                count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    sol.countPrimes(1)