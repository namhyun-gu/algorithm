# TODO Sliding Window로 구할 수 있다고 하는데 이해가 안 됨
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret, i, j = 0, 0, 0
        str_set = set()

        while i < len(s) and j < len(s):
            if s[j] not in str_set:
                str_set.add(s[j])
                j += 1
                ret = max(ret, j - i)
            else:
                str_set.remove(s[i])
                i += 1
        return ret


if __name__ == "__main__":
    sol = Solution()

    ret = sol.lengthOfLongestSubstring("abcabcbb")
    print(ret)  # Expect 3 ("abc")

    ret = sol.lengthOfLongestSubstring("bbbb")
    print(ret)  # Expect 1

    ret = sol.lengthOfLongestSubstring("pwwkew")
    print(ret)  # Expect 3 ("wke")

    ret = sol.lengthOfLongestSubstring("")
    print(ret)  # Expect 0
