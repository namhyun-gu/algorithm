import io
import sys

example = """
2
ifailuhkqq
kkkk
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
def sherlockAndAnagrams(s):
    ret = 0
    substr_dict = {}
    for i in range(len(s)):
        for j in range(len(s) - i):
            substr = "".join(sorted(s[j : j + i + 1]))
            substr_dict[substr] = substr_dict.get(substr, 0) + 1

    for key in substr_dict:
        ret += (substr_dict[key] - 1) * substr_dict[key] // 2
    return ret


if __name__ == "__main__":
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        print(result)