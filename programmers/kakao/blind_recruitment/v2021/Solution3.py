from collections import defaultdict
from bisect import bisect_left


def product(a, b):
    ret = []
    for _a in a:
        for _b in b:
            ret.append(_a + _b)
    return ret


def solution(info, query):
    answer = []
    group = defaultdict(list)
    for i in info:
        a, b, c, d, score = i.split()
        group["".join([a, b, c, d])].append(int(score))

    for _, value in group.items():
        value.sort()

    for q in query:
        a, _, b, _, c, _, d, score = q.split()
        score = int(score)
        keys = []

        if a != "-":
            keys.append(a)
        else:
            for lang in ["java", "python", "cpp"]:
                keys.append(lang)

        keys = product(keys, [b] if b != "-" else ["backend", "frontend"])
        keys = product(keys, [c] if c != "-" else ["senior", "junior"])
        keys = product(keys, [d] if d != "-" else ["pizza", "chicken"])

        count = 0
        for key in keys:
            count += len(group[key]) - bisect_left(group[key], score)
        answer.append(count)
    return answer


if __name__ == "__main__":
    info = [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50",
    ]
    query = [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150",
    ]
    ret = solution(info, query)
    print(ret)