dirs = [(0, 0), (1, 0), (0, 1), (1, 1)]


def can_remove(board, x, y):
    width = len(board[0])
    height = len(board)

    if x + 1 >= width or y + 1 >= height:
        return False

    return board[y][x] == board[y][x + 1] and board[y][x + 1] == board[y + 1][x] and board[y + 1][x] == board[y + 1][x + 1]


def remove(x, y):
    list = []
    for (dx, dy) in dirs:
        list.append((x + dx, y + dy))
    return list


def fill_board(board, m, n):
    for y in reversed(range(m)):
        for x in range(n):
            if board[y][x] == "":
                for upper in reversed(range(0, y - 1)):
                    if board[upper][x] != "":
                        board[y][x] = board[upper][x]
                        board[upper][x] = ""
                        break


def solution(m, n, board):
    board = list(map(list, board))
    removed = set()

    cnt = 0
    while True:
        for y in range(m):
            for x in range(n):
                if board[y][x] == "":
                    continue
                if can_remove(board, x, y):
                    for item in remove(x, y):
                        removed.add(item)

        if len(removed) == 0:
            break

        cnt += len(removed)
        for (remove_x, remove_y) in removed:
            board[remove_y][remove_x] = ""
        removed.clear()

        fill_board(board, m, n)

    return cnt


if __name__ == "__main__":
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(solution(2, 2, ["AA", "AA"]))
    print(solution(2, 2, ["AA", "AB"]))
    print(solution(3, 2, ["AA", "AA", "AB"]))
    print(solution(4, 2, ["CC", "AA", "AA", "CC"]))
    print(solution(6, 2, ["DD", "CC", "AA", "AA", "CC", "DD"]))  # 12
    print(solution(8, 2, ["FF", "AA", "CC",
                          "AA", "AA", "CC", "DD", "FF"]))  # 8
    print(solution(6, 2, ["AA", "AA", "CC", "AA", "AA", "DD"]))  # 8
