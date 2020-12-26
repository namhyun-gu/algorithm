# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
이 문제를 처음 접근할 때 다음과 같이 
앞선 노드의 값들을 하나씩 앞으로 가져오고
마지막 노드의 바로 앞 노드의 next 값을 Null로 변경하여 해결했다.

current = node
while current.next != None:
    current.val = current.next.val
    if current.next.next == None:
        current.next = None
    else:
        current = current.next

솔루션을 확인해보니 while 문 사용 없이
다음 두 줄로 문제를 해결할 수 있었는데

앞선 노드의 값을 가져오고,
하나 앞선 노드의 다음 노드 자리를 그 다음 노드로 옮기면 해결된다.

[4] -> [5] -> [1] -> [9] -> null : [5] 삭제

[4] -> [1] -> [1] -> [9] -> null

[4] -> [1] -> [9] -> null
"""


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next