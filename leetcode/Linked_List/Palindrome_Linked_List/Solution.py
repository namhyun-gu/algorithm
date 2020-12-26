# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True

        length = 0
        cur = head
        while cur != None:
            cur = cur.next
            length += 1

        stack = []
        cur = head
        half = length // 2
        for idx in range(length):
            if idx < half:
                stack.append(cur.val)
            else:
                if not (idx == half and length % 2):
                    if cur.val != stack.pop():
                        return False
            cur = cur.next
        return True


if __name__ == "__main__":
    sol = Solution()

    example1 = ListNode(1, ListNode(2))
    ret = sol.isPalindrome(example1)
    print(ret)  # Expect False

    example2 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    ret = sol.isPalindrome(example2)
    print(ret)  # Expect True

    example3 = ListNode(1, ListNode(0, ListNode(1)))
    ret = sol.isPalindrome(example3)
    print(ret)  # Exprect True
