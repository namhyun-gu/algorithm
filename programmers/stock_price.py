def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for idx in range(len(prices)):
        while stack and prices[stack[-1]] > prices[idx]:
            top = stack.pop()
            answer[top] = idx - top
        stack.append(idx)

    while stack:
        top = stack.pop()
        answer[top] = len(prices) - 1 - top

    return answer


if __name__ == "__main__":
    examples = [
        ({"prices": [1, 2, 3, 2, 3]}, [4, 3, 1, 1, 0]),
    ]

    for example, expected in examples:
        ret = solution(example["prices"])
        print("acutal:", ret, "expected:", expected)