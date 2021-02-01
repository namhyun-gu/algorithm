def solution(new_id: str):
    new_id = new_id.lower()

    new_id = "".join(filter(lambda s: s.isalnum() or s in ["-", "_", "."], new_id))

    while new_id.find("..") >= 0:
        new_id = new_id.replace("..", ".")

    if len(new_id) > 0 and new_id[0] == ".":
        new_id = new_id[1:]

    if len(new_id) > 0 and new_id[-1] == ".":
        new_id = new_id[:-1]

    if len(new_id) == 0:
        new_id = "a"

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]

    if len(new_id) <= 2:
        while len(new_id) <= 2:
            new_id += new_id[-1]

    return new_id


if __name__ == "__main__":
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution("z-+.^."))
    print(solution("=.="))
    print(solution("123_.def"))
    print(solution("abcdefghijklmn.p"))
    print(solution(".1."))
