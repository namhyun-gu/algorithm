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
    fun mergeTwoLists(l1: ListNode?, l2: ListNode?): ListNode? {
        if (l1 == null) {
            return l2
        }
        if (l2 == null) {
            return l1
        }

        var head = ListNode(0)
        var temp = head
        var temp1 = l1
        var temp2 = l2

        while (temp1 != null && temp2 != null) {
            if (temp1.`val` < temp2.`val`) {
                temp.next = temp1
                temp1 = temp1.next
            } else {
                temp.next = temp2
                temp2 = temp2.next
            }
            temp = temp.next!!
        }

        while (temp1 != null) {
            temp.next = temp1
            temp1 = temp1.next
            temp = temp.next!!
        }

        while (temp2 != null) {
            temp.next = temp2
            temp2 = temp2.next
            temp = temp.next!!
        }
        return head.next
    }
}

val a = ListNode(-9, ListNode(3))
val b = ListNode(5, ListNode(7))
printList(a)
printList(b)

printList(Solution().mergeTwoLists(a, b))

//#region
fun printList(head: ListNode?) {
    var cur: ListNode? = head
    val data = mutableListOf<Int>()
    while (cur != null) {
        data.add(cur.`val`)
        cur = cur.next
    }
    println(data.joinToString(" -> "))
}
//#endregion