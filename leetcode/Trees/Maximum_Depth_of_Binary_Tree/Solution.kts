import kotlin.math.max

data class TreeNode(val `val`: Int, var left: TreeNode? = null, var right: TreeNode? = null)

class Solution {
    fun maxDepth(root: TreeNode?): Int {
        if (root == null) {
            return 0
        }
        return traversalTree(root, 1)
    }

    fun traversalTree(root: TreeNode, depth: Int): Int {
        if (root.left != null || root.right != null) {
            var lDepth = 0
            var rDepth = 0
            if (root.left != null) {
                lDepth = traversalTree(root.left!!, depth + 1)
            }
            if (root.right != null) {
                rDepth = traversalTree(root.right!!, depth + 1)
            }
            return max(lDepth, rDepth)
        }
        return depth
    }
}

val example = TreeNode(
    3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))
)

val sol = Solution()

println(sol.maxDepth(example))

//#region Util Functions

//#endregion