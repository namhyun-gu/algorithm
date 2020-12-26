# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(next=head)
        length = 0
        current = head
        while current != None:
            length += 1
            current = current.next

        length -= n
        current = dummy
        for _ in range(length):
            current = current.next

        current.next = current.next.next
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    example1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol.removeNthFromEnd(example1, 2)

    example2 = ListNode(1)
    sol.removeNthFromEnd(example2, 1)

    example3 = ListNode(1, ListNode(2))
    sol.removeNthFromEnd(example3, 1)