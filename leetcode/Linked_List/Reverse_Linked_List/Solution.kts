/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
data class ListNode(val `val`: Int, var next: ListNode? = null)

class Solution {
    fun reverseList(head: ListNode?): ListNode? {
        var cur: ListNode? = head
        var temp: ListNode? = null
        while (cur != null) {
            val next = cur.next
            cur.next = temp
            temp = cur
            cur = next
        }
        return temp
    }
}

val head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
printList(head)
printList(Solution().reverseList(head))

//#region
fun printList(head: ListNode?) {
    var cur: ListNode? = head
    val data = mutableListOf<Int>()
    while (cur != null) {
        data.add(cur?.`val`!!)
        cur = cur?.next
    }
    println(data.joinToString(" -> "))
}
//#endregion