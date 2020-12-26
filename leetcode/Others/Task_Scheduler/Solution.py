from typing import List


from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)
        max_count = 0
        max_count_size = 0
        for _, count in task_counter.most_common():
            max_count = max(max_count, count)
            if count == max_count:
                max_count_size += 1
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_size)


if __name__ == "__main__":

    def _assert(actual, expect):
        print(
            f"{actual}"
            if actual == expect
            else f'Expect result "{expect}" but, "{actual}"'
        )

    sol = Solution()

    ret = sol.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2)
    _assert(ret, 8)

    ret = sol.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=0)
    _assert(ret, 6)

    ret = sol.leastInterval(
        tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2
    )
    _assert(ret, 16)

    ret = sol.leastInterval(
        tasks=["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], n=2
    )
    _assert(ret, 12)
