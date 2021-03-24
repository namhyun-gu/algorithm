def solution(name):
    counts = [0] * len(name)

    for idx, c in enumerate(name):
        up = ord(c) - ord("A")
        down = ord("Z") - ord(c) + 1

        counts[idx] = min(up, down)

    answer = sum(counts)
    cur = 0

    while True:
        counts[cur] = 0
        if sum(counts) == 0:
            break

        l, r = 1, 1
        while counts[cur - l] == 0:
            l += 1
        while counts[cur + r] == 0:
            r += 1

        if l < r:
            answer += l
            cur -= l
        else:
            answer += r
            cur += r

    return answer


if __name__ == "__main__":
    # ret = solution("JEROEN")
    # print(ret)

    ret = solution("JAZ")
    print(ret)