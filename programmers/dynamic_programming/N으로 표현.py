def solution(N, number):
    dp = [0]

    for i in range(1, 9):
        temp = set()
        temp.add(int(str(N) * i))

        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    temp.add(x + y)
                    temp.add(x - y)
                    temp.add(x * y)
                    if y != 0:
                        temp.add(x // y)
        if number in temp:
            return i
        else:
            dp.append(temp)
    return -1