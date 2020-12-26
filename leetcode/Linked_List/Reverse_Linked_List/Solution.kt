/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun reverseList(head: ListNode?): ListNode? {
        if (head != null) {
            val stack = Stack<ListNode>()
            var current = head!!
            stack.push(current)
            while (current.next != null) {
                current = current.next
                stack.push(current)
            }
            val newHead = current
            var temp = newHead
            while (!stack.isEmpty()) {
                val node = stack.pop()
                temp.next = node
                temp = node
            }
            temp.next = null
            return newHead
        } else {
            return head
        }
    }
}