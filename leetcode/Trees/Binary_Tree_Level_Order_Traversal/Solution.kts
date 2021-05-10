data class TreeNode(val `val`: Int, var left: TreeNode? = null, var right: TreeNode? = null)

class Solution {
    fun levelOrder(root: TreeNode?): List<List<Int>> {
        if (root == null) {
            return emptyList()
        }
        val tree = mutableListOf<MutableList<Int>>()
        traversal(tree, root, 0)
        return tree
    }

    fun traversal(tree: MutableList<MutableList<Int>>, root: TreeNode, depth: Int) {
        if (tree.size == depth) {
            tree.add(mutableListOf())
        }

        tree[depth].add(root.`val`)

        if (root.left != null) {
            traversal(tree, root.left!!, depth + 1)
        }
        if (root.right != null) {
            traversal(tree, root.right!!, depth + 1)
        }
    }
}

val example1 = TreeNode(
    3,
    TreeNode(
        9
    ),
    TreeNode(
        20,
        TreeNode(15),
        TreeNode(7)
    )
)

val example2 = TreeNode(
    1,
)

val example3 = null

val sol = Solution()
println(sol.levelOrder(example1))
println(sol.levelOrder(example2))
println(sol.levelOrder(example3))

//#region Util Functions

//#endregion