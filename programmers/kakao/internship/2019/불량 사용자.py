def is_match(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False

    for i in range(len(user_id)):
        if banned_id[i] == "*":
            continue

        if user_id[i] != banned_id[i]:
            return False

    return True


def dfs(user_id, banned_id, answer, depth=0, contain=set()):
    if depth == len(banned_id):
        answer.add("".join(sorted(contain)))
        return

    for id in user_id:
        if is_match(id, banned_id[depth]) and id not in contain:
            contain.add(id)
            dfs(user_id, banned_id, answer, depth + 1, contain)
            contain.remove(id)


def solution(user_id, banned_id):
    answer = set()
    dfs(user_id, banned_id, answer)
    return len(answer)


if __name__ == "__main__":
    ret = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
    print(ret)

    ret = solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]
    )
    print(ret)

    ret = solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["fr*d*", "*rodo", "******", "******"],
    )
    print(ret)
