import io
import sys

example = """
6 5
two times three is not four
two times two is four
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
def checkMagazine(magazine, note):
    word_map = dict()
    for word in magazine:
        if word in word_map:
            word_map[word] += 1
        else:
            word_map[word] = 1

    for word in note:
        if word in word_map:
            word_map[word] -= 1
            if word_map[word] == 0:
                del word_map[word]
        else:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
