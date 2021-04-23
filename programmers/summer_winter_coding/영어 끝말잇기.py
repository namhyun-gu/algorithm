def solution(n, words):
    word_set = set()
    count = dict()

    current = 0
    prev = ""
    for word in words:
        if current in count:
            count[current] += 1
        else:
            count[current] = 1

        if len(prev) == 0:
            prev = word
        else:
            if prev[-1] != word[0]:
                return [current + 1, count[current]]
            prev = word

        if word in word_set:
            return [current + 1, count[current]]
        else:
            word_set.add(word)

        current += 1
        current = current % n

    return [0, 0]


if __name__ == "__main__":
    print(
        solution(
            3,
            [
                "tank",
                "kick",
                "know",
                "wheel",
                "land",
                "dream",
                "mother",
                "robot",
                "tank",
            ],
        )
    )
    print(
        solution(
            5,
            [
                "hello",
                "observe",
                "effect",
                "take",
                "either",
                "recognize",
                "encourage",
                "ensure",
                "establish",
                "hang",
                "gather",
                "refer",
                "reference",
                "estimate",
                "executive",
            ],
        )
    )
    print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
