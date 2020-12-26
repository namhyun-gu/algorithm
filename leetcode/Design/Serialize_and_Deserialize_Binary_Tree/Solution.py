# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


from collections import deque


class Codec:
    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""

        data = []
        queue = deque([root])

        while queue:
            cur = queue.popleft()
            if cur != None:
                data.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                data.append("null")

        while data[-1] == "null":
            data.pop()
        return ",".join(data)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        nodes = list(map(self.to_node, data.split(",")))
        nodes = nodes[::-1]

        root = nodes.pop()
        queue = deque([root])

        while queue:
            cur = queue.popleft()
            if nodes:
                cur.left = nodes.pop()
                if cur.left:
                    queue.append(cur.left)
            if nodes:
                cur.right = nodes.pop()
                if cur.right:
                    queue.append(cur.right)

        return root

    def to_node(self, val: str) -> TreeNode:
        if val != "null":
            return TreeNode(int(val))
        else:
            return None


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

if __name__ == "__main__":
    codec = Codec()

    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    data = codec.serialize(root)
    ret = codec.deserialize(data)
    print(data, ret, sep=" -> ")

    root = None
    data = codec.serialize(root)
    ret = codec.deserialize(data)
    print(data, ret, sep=" -> ")

    root = TreeNode(1)
    data = codec.serialize(root)
    ret = codec.deserialize(data)
    print(data, ret, sep=" -> ")

    root = TreeNode(1, TreeNode(2))
    data = codec.serialize(root)
    ret = codec.deserialize(data)
    print(data, ret, sep=" -> ")

    root = TreeNode(
        1, TreeNode(2), TreeNode(3, TreeNode(4, TreeNode(6), TreeNode(7)), TreeNode(5))
    )
    data = codec.serialize(root)
    ret = codec.deserialize(data)
    print(data, ret, sep=" -> ")
