from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx - 1]:
                max_profit += prices[idx] - prices[idx - 1]
        return max_profit


import unittest


class SoltionTest(unittest.TestCase):
    def test_example1(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([7, 1, 5, 3, 6, 4]), 7)

    def test_example2(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([1, 2, 3, 4, 5]), 4)

    def test_example3(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([7, 6, 4, 3, 1]), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)