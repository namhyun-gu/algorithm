// #region Util Functions
fun printArray(arr: Array<IntArray>) {
    for (i in arr.indices) {
        for (j in arr[0].indices) {
            print("${arr[i][j]} ")
        }
        println()
    }
    println()
}
// #endregion

val arr = arrayOf(intArrayOf(1, 2, 3), intArrayOf(4, 5, 6), intArrayOf(7, 8, 9))

fun zip(vararg arrs: IntArray): Array<IntArray> {
    val minSize = arrs.map { it.size }.minOrNull() ?: return emptyArray<IntArray>()
    val arr = Array<IntArray>(minSize) { idx ->
        arrs.map { it -> it[idx] }.toIntArray()
    }
    return arr
}

// 1. 2차원 배열 전치
fun transpose(arr: Array<IntArray>): Array<IntArray> {
    return zip(*arr)
}

printArray(transpose(arr))

// 2. 2차원 배열 회전 (시계 방향 90도)
//    반시계 방향 회전이 필요하면 arr내 있는 모든 배열을 반대로 뒤집어야 함
fun rotate(arr: Array<IntArray>): Array<IntArray> {
    return zip(*arr.reversedArray())
}

printArray(rotate(arr))