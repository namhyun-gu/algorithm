from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        intervals.sort()

        for s, e in intervals:
            if len(ret) > 0:
                last_s, last_e = ret[-1]

            if len(ret) == 0 or s > last_e:
                ret.append([s, e])
            elif e > last_e:
                ret[-1][1] = e
        return ret


if __name__ == "__main__":
    sol = Solution()

    ret = sol.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]])
    print(ret)  # Expect [[1,6],[8,10],[15,18]]

    ret = sol.merge(intervals=[[1, 4], [4, 5]])
    print(ret)  # Expect [[1,5]]
