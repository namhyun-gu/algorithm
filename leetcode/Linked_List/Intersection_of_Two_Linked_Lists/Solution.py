from __future__ import annotations

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next: ListNode = None):
        self.val = x
        self.next = next


# TODO 왜 이게 정답??
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None

        tempA = headA
        tempB = headB

        while tempA != tempB:
            tempA = headB if tempA == None else tempA.next
            tempB = headA if tempB == None else tempB.next
        return tempA


def to_linked_list(list: list[int]) -> ListNode:
    head = ListNode(-1)
    cur = head
    for item in list:
        node = ListNode(item)
        cur.next = node
        cur = node
    return head.next


def print_linked_list(head: ListNode):
    list = []
    while head != None:
        list.append(head.val)
        head = head.next
    list_str = ", ".join(map(str, list))
    print(f"[{list_str}]")


if __name__ == "__main__":
    sol = Solution()

    headA = to_linked_list([4, 1, 8, 4, 5])
    headB = to_linked_list([5, 6, 1, 8, 4, 5])

    ret = sol.getIntersectionNode(headA, headB)
    print_linked_list(ret)

    headA = to_linked_list([1, 9, 1, 2, 4])
    headB = to_linked_list([3, 2, 4])

    ret = sol.getIntersectionNode(headA, headB)
    print_linked_list(ret)

    headA = to_linked_list([2, 6, 4])
    headB = to_linked_list([1, 5])

    ret = sol.getIntersectionNode(headA, headB)
    print_linked_list(ret)
