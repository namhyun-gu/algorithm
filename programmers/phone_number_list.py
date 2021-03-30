def solution(phone_book):
    phone_book = sorted(phone_book, reverse=True)

    hash = set()
    while phone_book:
        shortest = phone_book.pop()
        hash.add(shortest)
        for idx in reversed(range(len(phone_book))):
            if phone_book[idx][: len(shortest)] in hash:
                return False
            else:
                break
    return True


if __name__ == "__main__":
    examples = [
        ({"phone_book": ["119", "97674223", "1195524421"]}, False),
        ({"phone_book": ["123", "456", "789"]}, True),
        ({"phone_book": ["12", "123", "1235", "567", "88"]}, False),
    ]

    for example, expected in examples:
        ret = solution(example["phone_book"])
        print("acutal:", ret, "expected:", expected)