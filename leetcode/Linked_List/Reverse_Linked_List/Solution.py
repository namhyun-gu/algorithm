# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    result = Solution().reverseList(head)
    print(result)