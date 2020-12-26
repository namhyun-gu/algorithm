from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 200
        for str in strs:
            min_len = min(min_len, len(str))

        if min_len == 0 or len(strs) == 0:
            return ""

        lcp = ""
        for idx in range(min_len):
            is_common = True
            cmp = strs[0][idx]
            for str in strs:
                if str[idx] != cmp:
                    is_common = False
                    break
            if is_common:
                lcp += cmp
            else:
                break
        return lcp