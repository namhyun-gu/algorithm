# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode()

        cur = ret
        prev = None
        carry = 0
        while l1 and l2:
            cur.val = l1.val + l2.val + carry
            if cur.val >= 10:
                cur.val -= 10
                carry = 1
            else:
                carry = 0

            l1 = l1.next
            l2 = l2.next
            prev = cur
            cur.next = ListNode()
            cur = cur.next

        while l1:
            cur.val = l1.val + carry
            if cur.val >= 10:
                cur.val -= 10
                carry = 1
            else:
                carry = 0

            l1 = l1.next
            prev = cur
            cur.next = ListNode()
            cur = cur.next

        while l2:
            cur.val = l2.val + carry
            if cur.val >= 10:
                cur.val -= 10
                carry = 1
            else:
                carry = 0

            l2 = l2.next
            prev = cur
            cur.next = ListNode()
            cur = cur.next

        if carry:
            cur.val = carry
        else:
            prev.next = None
        return ret


def print_node(node: ListNode):
    while node:
        print(node.val, end=", ")
        node = node.next
    print()


if __name__ == "__main__":
    sol = Solution()

    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    ret = sol.addTwoNumbers(l1, l2)
    print_node(ret)

    l1 = ListNode(
        9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
    )
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    ret = sol.addTwoNumbers(l1, l2)
    print_node(ret)

    l1 = ListNode(0)
    l2 = ListNode(0)
    ret = sol.addTwoNumbers(l1, l2)
    print_node(ret)

    l1 = ListNode(2, ListNode(4, ListNode(9)))
    l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
    ret = sol.addTwoNumbers(l1, l2)
    print_node(ret)