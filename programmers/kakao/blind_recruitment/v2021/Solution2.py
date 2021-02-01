from itertools import combinations
from collections import Counter, defaultdict


def solution(orders, course):
    combs = defaultdict(list)
    for order in orders:
        for size in course:
            combs[size] += map("".join, combinations(sorted(order), size))

    comb_counts = []
    for comb in combs.values():
        comb_counts.append(Counter(comb).most_common())

    answer = []
    for comb_count in comb_counts:
        if not comb_count:
            continue

        most_count = comb_count[0][1]
        if most_count < 2:
            continue

        for comb, count in comb_count:
            if count == most_count:
                answer.append(comb)
            else:
                break
    return sorted(answer)


if __name__ == "__main__":
    ret = solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
    print(ret)

    ret = solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])
    print(ret)

    ret = solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
    print(ret)