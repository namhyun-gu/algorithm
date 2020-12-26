# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        odd: ListNode = None
        even: ListNode = None

        odd_head = None
        even_head = None

        idx = 0
        while head:
            if idx % 2:
                if odd:
                    odd.next = head
                    odd = odd.next
                else:
                    odd = head
                    odd_head = odd
            else:
                if even:
                    even.next = head
                    even = even.next
                else:
                    even = head
                    even_head = even
            head = head.next
            idx += 1

        even.next = odd_head
        if odd:
            odd.next = None
        return even_head


def print_node(node: ListNode):
    while node:
        print(node.val, end=", ")
        node = node.next
    print()


if __name__ == "__main__":
    sol = Solution()

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    ret = sol.oddEvenList(head)
    print_node(ret)

    head = ListNode(
        2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7))))))
    )
    ret = sol.oddEvenList(head)
    print_node(ret)

    head = ListNode(1)
    ret = sol.oddEvenList(head)
    print_node(ret)