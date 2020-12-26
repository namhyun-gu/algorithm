class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                break

            if haystack[i] == needle[0]:
                find = True
                for j in range(len(needle)):
                    if i + j < len(haystack):
                        if haystack[i + j] != needle[j]:
                            find = False
                            break
                    else:
                        find = False
                        break
                if find:
                    return i
        return -1
