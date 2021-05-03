def can_move(stones, k, count):
    temp = list(stones)

    for idx in range(len(stones)):
        temp[idx] -= count

    # 연속으로 0인 구간 찾기
    cnt = 0
    for idx in range(len(stones)):
        if temp[idx] <= 0:
            cnt += 1
        else:
            cnt = 0

        if cnt >= k:
            return False
    return True


def solution(stones, k):
    l, r = 1, 200_000_000

    while l <= r:
        mid = (l + r) // 2

        if can_move(stones, k, mid):
            l = mid + 1
        else:
            r = mid - 1

    return l


if __name__ == "__main__":
    ret = solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
    print(ret)