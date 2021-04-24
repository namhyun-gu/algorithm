# region Util Functions
def print_arr(arr):
    for i in range(len(arr)):
        print("[", end="")
        for j in range(len(arr[0])):
            if j < len(arr[0]) - 1:
                print(arr[i][j], end=", ")
            else:
                print(arr[i][j], end="]\n")
    print()


# endregion

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# 1. 2차원 배열 전치
print("# Transpose\n")

for _ in range(2):
    arr = list(zip(*arr))
    print_arr(arr)

# 2. 2차원 배열 회전
print("# Rotate\n")

for _ in range(4):
    arr = list(zip(*arr[::-1]))
    print_arr(arr)