def pick(board, move):
    selected = None
    for row in range(len(board)):
        if board[row][move] != 0:
            selected = board[row][move]
            board[row][move] = 0
            break
    return selected


def solution(board, moves):
    answer = 0
    bucket = []

    for move in moves:
        move -= 1

        selected = pick(board, move)
        if selected:
            if bucket and bucket[-1] == selected:
                bucket.pop()
                answer += 2
            else:
                bucket.append(selected)

    return answer


if __name__ == "__main__":
    ret = solution(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 3],
            [0, 2, 5, 0, 1],
            [4, 2, 4, 4, 2],
            [3, 5, 1, 3, 1],
        ],
        [1, 5, 3, 5, 1, 2, 1, 4],
    )
    print(ret)
