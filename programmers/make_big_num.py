def solution(number, k):
    answer = []
    idx = 0
    for s in range(len(number) - k):
        big = "0"
        for i in range(idx, s + k + 1):
            if number[i] > big:
                big = number[i]
                idx = i + 1

                if big == "9":
                    break
        answer.append(big)
    return "".join(answer)


if __name__ == "__main__":
    for number, k in [("1924", 2), ("1231234", 3), ("4177252841", 4)]:
        ret = solution(number, k)
        print(ret)