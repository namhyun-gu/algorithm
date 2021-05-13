data class ListNode(var `val`: Int, var next: ListNode? = null)

class Solution {
    fun hasCycle(head: ListNode?): Boolean {
        var slow = head
        var fast = head
        
        while (slow?.next != null && fast?.next?.next != null) {
            slow = slow.next
            fast = fast.next?.next
            
            if (slow == fast) {
                return true
            }
        }
        return false
    }
}

fun makeCycle(node: ListNode, pos: Int) {
    var cur: ListNode? = node
    repeat(pos) {
        cur = cur?.next
    }
    var target = cur
    while (cur?.next != null) {
        cur = cur?.next
    }
    cur?.next = target
}

val sol = Solution()
val example1 = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
makeCycle(example1, 1)
sol.hasCycle(example1)

val sol = Solution()
val example2 = ListNode(1, ListNode(2))
makeCycle(example2, 0)
sol.hasCycle(example2)

val sol = Solution()
val example3 = ListNode(1)
sol.hasCycle(example3)

val sol = Solution()
val example4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
sol.hasCycle(example4)


