data class ListNode(var `val`: Int, var next: ListNode? = null)

fun printNode(node: ListNode?) {
    if (node == null) {
        println("null")
    }
    
    var cur: ListNode? = node
    while (cur != null) {
        print("${cur.`val`} -> ")
        cur = cur.next
    }
    println()
}

class Solution {
    fun removeNthFromEnd(head: ListNode?, n: Int): ListNode? {
        val temp = ListNode(0, head)
        var length = 0
        var cur: ListNode? = head
        
        while (cur != null) {
            cur = cur.next
            length++
        }
        
        cur = temp
        repeat(length - n) {
            cur = cur?.next
        }
        cur!!.next = cur!!.next?.next
        return temp.next
    }
}

val head = ListNode(
    1, ListNode(
        2, ListNode(
            3, ListNode(
                4, ListNode(5)
            )
        )
    )
)

printNode(head)
printNode(Solution().removeNthFromEnd(head, 2))