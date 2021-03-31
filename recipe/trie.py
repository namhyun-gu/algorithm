# %%
class Node:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, key):
        cur = self.root
        # 주어지는 문자열을 반복하여
        # 해당 문자가 노드의 Map에 존재하는지를 확인하고,
        #
        # 존재하지 않는다면,
        # 노드의 Map의 해당 문자에 새 노드를 추가한다.
        #
        # 다음 문자를 추가하기 위해
        # 현재 노드를 노드의 Map에 있는 현재 문자에 대한 노드로 교체한다.
        for c in key:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        # 모든 문자를 반복하여 끝났다면 현재 노드에 문자열의 마지막임을 저장한다.
        cur.end_of_word = True

    def find(self, key):
        cur = self.root
        # 주어지는 문자열을 반복하여,
        # 해당 문자가 노드의 Map에 존재하는 지 확인하고,
        #
        # 존재하지 않는다면,
        # 이 문자열은 Trie에 저장되지 않았으므로 `False`를 반환한다.
        #
        # 존재한다면,
        # 다음 문자를 확인하기 위해 현재 노드를 노드의 Map에 있는 현재 문자에 대한 노드로 교체한다.
        for c in key:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        # 모든 문자를 반복하여 끝났다면 해당 노드가 문자열의 마지막임 저장한 값을 반환한다.
        # e.g ABC를 삽입하고 나서, ABC에 대해 찾았다면 해당 노드의 `end_of_word`는 True
        return cur.end_of_word


trie = Trie()
trie.insert("ABC")
trie.find("ABC")