# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged_head = None
        merged = None

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                if merged:
                    merged.next = l1
                    merged = l1
                else:
                    merged_head = l1
                    merged = l1
                l1 = l1.next
            else:
                if merged:
                    merged.next = l2
                    merged = l2
                else:
                    merged_head = l2
                    merged = l2
                l2 = l2.next

        while l1 != None:
            if merged:
                merged.next = l1
                merged = l1
            else:
                merged_head = l1
                merged = l1
            l1 = l1.next

        while l2 != None:
            if merged:
                merged.next = l2
                merged = l2
            else:
                merged_head = l2
                merged = l2
            l2 = l2.next

        if merged != None:
            merged.next = None

        return merged_head