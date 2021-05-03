from collections import defaultdict
from heapq import heappush


def solution(gems):
    all_gems = set(gems)

    in_gems = defaultdict(int)
    in_gems[gems[0]] += 1

    answer = []

    l, r = 0, 0
    while l < len(gems) and r < len(gems):
        if len(in_gems) < len(all_gems):
            r += 1
            if r in range(len(gems)):
                in_gems[gems[r]] += 1
        else:
            heappush(answer, (r - l, l, r))
            in_gems[gems[l]] -= 1
            if in_gems[gems[l]] == 0:
                del in_gems[gems[l]]
            l += 1

    _, ans_l, ans_r = answer[0]
    ans_l += 1
    ans_r += 1
    return [ans_l, ans_r]


if __name__ == "__main__":
    ret = solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
    print(ret)

    ret = solution(["AA", "AB", "AC", "AA", "AC"])
    print(ret)

    ret = solution(["XYZ", "XYZ", "XYZ"])
    print(ret)

    ret = solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
    print(ret)