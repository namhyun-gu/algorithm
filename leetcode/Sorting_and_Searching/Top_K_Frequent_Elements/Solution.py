from typing import List

import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = dict()

        for num in nums:
            if num in frequent:
                frequent[num] += 1
            else:
                frequent[num] = 1

        frequent_list = []
        for num, count in frequent.items():
            heapq.heappush(frequent_list, (-count, num))

        ret = []
        for _ in range(k):
            top = heapq.heappop(frequent_list)
            ret.append(top[1])
        return ret


if __name__ == "__main__":
    sol = Solution()

    ret = sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    print(ret)

    ret = sol.topKFrequent([1], 1)
    print(ret)