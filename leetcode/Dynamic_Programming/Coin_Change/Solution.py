from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount + 1 for _ in range(amount + 1)]
        memo[0] = 0
        for n in range(1, amount + 1):
            for coin in coins:
                if n >= coin:
                    memo[n] = min(memo[n], memo[n - coin] + 1)

        if memo[amount] > amount:
            return -1
        return memo[amount]


if __name__ == "__main__":
    sol = Solution()

    ret = sol.coinChange(coins=[1, 2, 5], amount=11)
    print(ret)  # Expect 3

    ret = sol.coinChange(coins=[2], amount=3)
    print(ret)  # Expect -1

    ret = sol.coinChange(coins=[1], amount=0)
    print(ret)  # Expect 0

    ret = sol.coinChange(coins=[1], amount=1)
    print(ret)  # Expect 1

    ret = sol.coinChange(coins=[1], amount=2)
    print(ret)  # Expect 2
