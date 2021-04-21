data class ListNode(var `val`: Int, var next: ListNode? = null)

fun printNode(node: ListNode?) {
    var cur: ListNode? = node
    while (cur != null) {
        print("${cur.`val`} -> ")
        cur = cur.next
    }
    println()
}

class Solution {
    fun deleteNode(node: ListNode?) {
        if (node != null && node.next != null) {
            node.`val` = node.next!!.`val`
            node.next = node.next!!.next
        }
    }
}

val node = ListNode(
    5, ListNode(
        1, ListNode(9)
    )
)

val head = ListNode(
    4, node
)

printNode(head)
Solution().deleteNode(node)
printNode(head)