def to_tuple_list(s):
    ret = []
    temp = []
    stack = []

    s = s[1:-1]

    for c in s:
        if c == "{":
            stack.append(c)
        elif c == "}":
            stack.append(c)
            ret.append("".join(temp).split(","))
            temp = []
        elif c == "," and stack[-1] == "}":
            continue
        else:
            temp.append(c)
    return ret


def diff(a, b):
    a = set(a)
    b = set(b)
    return list(b.difference(a))[0]


def solution(s):
    answer = []
    l = to_tuple_list(s)
    l.sort(key=len)

    answer.append(l[0][0])

    for i in range(1, len(l)):
        answer.append(diff(l[i - 1], l[i]))

    return list(map(int, answer))


if __name__ == "__main__":
    ret = solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
    print(ret)

    ret = solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
    print(ret)

    ret = solution("{{20,111},{111}}")
    print(ret)

    ret = solution("{{123}}")
    print(ret)

    ret = solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")
    print(ret)
