import io
import sys

example = """
5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink
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
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.end_of_word


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())

    trie = Trie()
    for _ in range(N):
        trie.insert(input().rstrip())

    cnt = 0
    for _ in range(M):
        if trie.find(input().rstrip()):
            cnt += 1

    print(cnt)