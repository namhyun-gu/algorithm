class Solution:
    def to_dict(self, s: str):
        s_dict = dict()

        for c in s:
            if c not in s_dict:
                s_dict[c] = 1
            else:
                s_dict[c] += 1
        return s_dict

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = self.to_dict(s)
        t_dict = self.to_dict(t)

        if s_dict.keys() == t_dict.keys():
            for key in s_dict.keys():
                if s_dict[key] != t_dict[key]:
                    return False
            return True
        else:
            return False
