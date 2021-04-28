import java.io.ByteArrayInputStream
import java.util.*

fun main() = with(Scanner(System.`in`)) {
    var tc = 0
    while (true) {
        tc += 1

        val nodes = mutableSetOf<Int>()
        val indegrees = mutableMapOf<Int, Int>()
        var edges = 0

        while (true) {
            val u = nextInt()
            val v = nextInt()

            if (u == 0 && v == 0) {
                break
            }
            if (u == -1 && v == -1) {
                return
            }
            nodes.add(u)
            nodes.add(v)
            indegrees[v] = indegrees.getOrDefault(v, 0) + 1
            edges += 1
        }

        if (nodes.size == 0) {
            println("Case $tc is a tree.")
            continue
        }

        var hasTwoIndegrees = false
        var root = 0

        for (node in nodes) {
            if (node !in indegrees) {
                root += 1
            } else if (indegrees[node]!! > 1) {
                hasTwoIndegrees = true
                break
            }
        }

        if (hasTwoIndegrees || root != 1 || nodes.size != edges + 1) {
            println("Case $tc is not a tree.")
        } else {
            println("Case $tc is a tree.")
        }
    }
}

// #region Set Input
fun main(args: Array<String>) {
    val example = """6 8  5 3  5 2  6 4
5 6  0 0

8 1  7 3  6 2  8 9  7 5
7 4  7 8  7 6  0 0

3 8  6 8  6 4
5 3  5 6  5 2  0 0
-1 -1""".trimIndent()

    System.setIn(ByteArrayInputStream(example.toByteArray()))

    main()
}
// #endregion