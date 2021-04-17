def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        num = absolutes[i]
        if not signs[i]:
            num *= -1
        answer += num
    return answer