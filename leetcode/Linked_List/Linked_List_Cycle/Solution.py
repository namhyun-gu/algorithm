# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False

        first = head
        second = head.next

        while first != second:
            if second == None or second.next == None:
                return False
            first = first.next
            second = second.next.next
        return True


if __name__ == "__main__":
    sol = Solution()

    node4 = ListNode(-4)
    node3 = ListNode(0)
    node3.next = node4
    node2 = ListNode(2)
    node2.next = node3
    node1 = ListNode(3)
    node1.next = node2

    node4.next = node2

    example1 = node1

    print(sol.hasCycle(example1))