# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        """
        이 방법으로 해결은 했으나 추가 공간을 사용했는데
        아래의 재귀로 추가 공간 없이 구현할 수 있다.

        def connect(self, root):
            self._connect(root, None)
            return root

        def _connect(self, cur, next):
            if cur == None: return
            cur.next = next
            self._connect(cur.left, cur.right)
            self._connect(cur.right, cur.next.left if cur.next else None)

        Ref: leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/789/discuss/37472/A-simple-accepted-solution/265892
        """
        if root:
            self._connect([root])
        return root

    def _connect(self, nodes: list["Node"]):
        if nodes:
            prev: "Node" = None
            next_nodes = []
            for node in nodes:
                if prev:
                    prev.next = node
                prev = node

                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            self._connect(next_nodes)


def printTree(root: Node):
    queue = [root]

    while queue:
        cur = queue.pop(0)

        left = cur.left.val if cur.left else "none"
        right = cur.right.val if cur.right else "none"
        next = cur.next.val if cur.next else "none"
        print(f"val: {cur.val}, left: {left}, right: {right}, next: {next}")

        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)


if __name__ == "__main__":
    sol = Solution()

    root = Node(
        1,
        left=Node(2, left=Node(4), right=Node(5)),
        right=Node(3, left=Node(6), right=Node(7)),
    )
    ret = sol.connect(root)
    printTree(ret)