import collections


def solution(people, limit):
    answer = 0
    people = sorted(people)
    queue = collections.deque(people)

    while queue:
        a = queue.pop()
        if queue and a + queue[0] <= limit:
            queue.popleft()
        answer += 1
    return answer


if __name__ == "__main__":
    examples = [
        ({"people": [70, 50, 80, 50], "limit": 100}, 3),
        ({"people": [70, 80, 50], "limit": 100}, 3),
    ]

    for example, expected in examples:
        ret = solution(example["people"], example["limit"])
        print("acutal:", ret, "expected:", expected)