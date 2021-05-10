data class TreeNode(val `val`: Int, var left: TreeNode? = null, var right: TreeNode? = null)

class Solution {
    fun isValidBST(root: TreeNode?): Boolean {
        return validNode(root, null, null)
    }

    fun validNode(root: TreeNode?, min: Int?, max: Int?): Boolean {
        if (root == null) {
            return true
        }
        if (min != null && root.`val` <= min) {
            return false
        }
        if (max != null && root.`val` >= max) {
            return false
        }
        return validNode(root.left, min, root.`val`) && validNode(root.right, root.`val`, max)
    }
}

val example1 = TreeNode(
    2, TreeNode(1), TreeNode(3)
)

val example2 = TreeNode(
    5, TreeNode(1), TreeNode(
        4,
        TreeNode(3), TreeNode(6)
    )
)

val example3 = TreeNode(
    5, TreeNode(1), TreeNode(
        4,
        TreeNode(3), TreeNode(6)
    )
)

val sol = Solution()
println(sol.isValidBST(example1))
println(sol.isValidBST(example2))
println(sol.isValidBST(example3))

//#region Util Functions

//#endregion