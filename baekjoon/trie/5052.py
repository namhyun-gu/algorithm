import io
import sys

example = """
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, key):
        cur = self.root
        for ch in key:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.end_of_word = True

    def find(self, key):
        cur = self.root
        for ch in key:
            if cur.end_of_word:
                return False
            cur = cur.children[ch]
        return True


if __name__ == "__main__":
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        trie = Trie()
        n = int(input())
        numbers = []

        for _ in range(n):
            number = input().rstrip()
            trie.insert(number)
            numbers.append(number)
        
        consistency = True
        for number in numbers:
            if not trie.find(number):
                consistency = False

        if consistency:
            print("YES")
        else:
            print("NO")
