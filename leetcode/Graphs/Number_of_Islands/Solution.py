from typing import List

from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue, visit = deque(), set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            queue.append((r, c))
            while queue:
                r, c = queue.popleft()
                for dr, dc in dirs:
                    tr, tc = r + dr, c + dc
                    # * range로 범위에 있는지 확인할 수 있다.
                    if tr in range(rows) and tc in range(cols):
                        if grid[tr][tc] == "1" and (tr, tc) not in visit:
                            queue.append((tr, tc))
                            visit.add((tr, tc))

        ret = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    ret += 1
        return ret


if __name__ == "__main__":
    sol = Solution()

    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    ret = sol.numIslands(grid)
    print(ret)  # Expect 1

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    ret = sol.numIslands(grid)
    print(ret)  # Expect 3
