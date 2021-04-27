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
    fun isPalindrome(head: ListNode?): Boolean {
        var fast = head
        var slow = head

        // fast가 null이 될 때 slow는 전체 리스트의 중간 지점에 도착하게 된다
        while (fast?.next != null) {
            fast = fast.next?.next
            slow = slow?.next
        }

        if (fast != null) { // If Odd length.
            slow = slow?.next
        }

        fast = head
        slow = reverseList(slow)

        while (slow != null) {
            if (fast?.`val` != slow.`val`) {
                return false
            }
            fast = fast.next
            slow = slow.next
        }
        return true
    }

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

val sol = Solution()

val example1 = toList(intArrayOf(1, 2, 2, 1))
printList(example1)
println(sol.isPalindrome(example1))

val example2 = toList(intArrayOf(1, 2))
printList(example2)
println(sol.isPalindrome(example2))

//#region Util Functions
fun printList(head: ListNode?) {
    var cur: ListNode? = head
    val data = mutableListOf<Int>()
    while (cur != null) {
        data.add(cur!!.`val`)
        cur = cur!!.next
    }
    println(data.joinToString(" -> "))
}

fun toList(arr: IntArray): ListNode {
    val head = ListNode(arr[0])
    var temp = head
    for (i in 1 until arr.size) {
        temp.next = ListNode(arr[i])
        temp = temp.next!!
    }
    return head
}
//#endregion