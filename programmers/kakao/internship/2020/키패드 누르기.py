keypad = {
    1: "L",
    2: "N",
    3: "R",
    4: "L",
    5: "N",
    6: "R",
    7: "L",
    8: "N",
    9: "R",
    0: "N",
}

keypad_pos = {
    1: (0, 0),
    2: (1, 0),
    3: (2, 0),
    4: (0, 1),
    5: (1, 1),
    6: (2, 1),
    7: (0, 2),
    8: (1, 2),
    9: (2, 2),
    0: (1, 3),
}


def dist(a, b):
    ax, ay = a
    bx, by = b

    return abs(ax - bx) + abs(ay - by)


def solution(numbers, hand):
    answer = []
    l = 0, 3
    r = 2, 3

    for number in numbers:
        if keypad[number] == "L":
            l = keypad_pos[number]
            answer.append(keypad[number])
        elif keypad[number] == "R":
            r = keypad_pos[number]
            answer.append(keypad[number])
        else:
            l_dist = dist(l, keypad_pos[number])
            r_dist = dist(r, keypad_pos[number])

            if l_dist < r_dist:
                l = keypad_pos[number]
                answer.append("L")
            elif l_dist > r_dist:
                r = keypad_pos[number]
                answer.append("R")
            else:
                if hand == "left":
                    l = keypad_pos[number]
                    answer.append("L")
                else:
                    r = keypad_pos[number]
                    answer.append("R")

    return "".join(answer)


if __name__ == "__main__":
    # ret = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
    # print(ret)

    ret = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
    print(ret)

    # ret = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")
    # print(ret)
