def jumpingOnClouds(c):
    jump = 0
    cur = 0
    end = len(c) - 1

    while cur < end:
        if cur + 2 <= end and c[cur + 2] != 1:
            cur += 2
        elif cur + 1 <= end and c[cur + 1] != 1:
            cur += 1
        jump += 1

    return jump


if __name__ == "__main__":
    ret = jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
    print(ret)