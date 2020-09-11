class TrieNode(object):
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False


class Trie(object):
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, key: str):
        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.endOfWord = True

    def find(self, key: str) -> bool:
        current = self.root
        for char in key:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.endOfWord


if __name__ == "__main__":
    trie = Trie()
    trie.insert("abc")
    trie.insert("ade")
    trie.insert("cbe")

    assert trie.find("abc") == True
    assert trie.find("ade") == True
    assert trie.find("cda") == False
