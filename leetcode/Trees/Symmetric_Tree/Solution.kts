data class TreeNode(val `val`: Int, var left: TreeNode? = null, var right: TreeNode? = null)

class Solution {
    fun isSymmetric(root: TreeNode?): Boolean {
        if (root == null) {
            return true
        }
        return symmetric(root.left, root.right)
    }

    fun symmetric(left: TreeNode?, right: TreeNode?): Boolean {
        if (left?.`val` != right?.`val`) {
            return false
        }

        if (left != null && right != null) {
            return symmetric(left.left, right.right) && symmetric(left.right, right.left)
        }
        return true
    }
}

val example1 = TreeNode(
    1,
    TreeNode(
        2,
        TreeNode(3),
        TreeNode(4)
    ),
    TreeNode(
        2,
        TreeNode(3),
        TreeNode(4)
    )
)

val example2 = TreeNode(
    1,
    TreeNode(2, right = TreeNode(3)),
    TreeNode(2, right = TreeNode(3))
)

val sol = Solution()
println(sol.isSymmetric(example1))
println(sol.isSymmetric(example2))

//#region Util Functions

//#endregion