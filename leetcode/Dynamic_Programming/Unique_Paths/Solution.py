from collections import deque


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(n)] for _ in range(m)]
        memo[0][0] = 1

        for y in range(m):
            for x in range(n):
                if x == 0 and y == 0:
                    continue
                if y > 0:
                    memo[y][x] += memo[y - 1][x]
                if x > 0:
                    memo[y][x] += memo[y][x - 1]
        return memo[-1][-1]


if __name__ == "__main__":
    sol = Solution()

    ret = sol.uniquePaths(3, 7)
    print(ret)

    ret = sol.uniquePaths(3, 2)
    print(ret)

    ret = sol.uniquePaths(7, 3)
    print(ret)

    ret = sol.uniquePaths(3, 3)
    print(ret)