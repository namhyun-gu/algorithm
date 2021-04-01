import io
import sys

example = """
Red Alder
Ash
Aspen
Basswood
Ash
Beech
Yellow Birch
Ash
Cherry
Cottonwood
Ash
Cypress
Red Elm
Gum
Hackberry
White Oak
Hickory
Pecan
Hard Maple
White Oak
Soft Maple
Red Oak
Red Oak
White Oak
Poplan
Sassafras
Sycamore
Black Walnut
Willow
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


class Node:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, key):
        cur = self.root
        for c in key:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end_of_word = True

    def find(self, key):
        cur = self.root
        for c in key:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end_of_word


if __name__ == "__main__":
    input = sys.stdin.readline

    trie = Trie()
    word_dict = {}
    cnt = 0

    while True:
        word = input().rstrip()
        if not word:
            break

        if trie.find(word):
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            trie.insert(word)
        cnt += 1

    for key in sorted(word_dict.keys()):
        print(key, format((word_dict[key] / cnt) * 100, ".4f"))