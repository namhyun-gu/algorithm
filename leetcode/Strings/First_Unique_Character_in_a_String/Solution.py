class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1

        char_dict = dict()
        for idx, c in enumerate(s):
            if c not in char_dict:
                char_dict[c] = idx
            else:
                char_dict[c] = -1

        min_idx = len(s)
        for key in char_dict.keys():
            if char_dict[key] != -1:
                min_idx = min(min_idx, char_dict[key])

        if min_idx == len(s):
            return -1
            
        return min_idx
        