import io
import sys

example = """
4
2 KIWI BANANA
2 KIWI APPLE
2 APPLE APPLE
3 APPLE BANANA KIWI
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

    def print_tree(self, node=None, depth=0):
        if node == None:
            node = self.root

        for key in sorted(node.children.keys()):
            prefix = "--" * depth
            print(prefix + key)

            self.print_tree(node.children[key], depth + 1)


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    trie = Trie()

    for _ in range(N):
        _, *food = input().split()
        trie.insert(food)

    trie.print_tree()
