from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = dict()
        for s in strs:
            key = "".join(sorted(s))
            if key in group:
                group[key].append(s)
            else:
                group[key] = [s]
        return list(map(lambda item: item[1], group.items()))


if __name__ == "__main__":
    sol = Solution()

    ret = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(ret)  # Expect [["bat"],["nat","tan"],["ate","eat","tea"]]

    ret = sol.groupAnagrams([""])
    print(ret)  # Expect [[""]]

    ret = sol.groupAnagrams(["a"])
    print(ret)  # Expect [["a"]]

    ret = sol.groupAnagrams(["ddddddddddg", "dgggggggggg"])
    print(ret)  # Expect [["dgggggggggg"],["ddddddddddg"]]
