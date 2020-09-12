from collections import deque

board = [
    [0, 0, 1],
    [0, 1, 1],
    [0, 0, 0]
]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(x: int = 0, y: int = 0, visited: list = [(0, 0)]):
    if x == len(board) - 1 and y == len(board) - 1:
        return

    for (dx, dy) in dirs:
        nextx = x + dx
        nexty = y + dy

        if nextx < 0 or nexty < 0 or nextx >= len(board) or nexty >= len(board):
            continue

        if (nextx, nexty) not in visited:
            visited.append((nextx, nexty))
            print("({}, {})".format(nextx, nexty))
            dfs(nextx, nexty, visited)
            visited.remove((nextx, nexty))


def bfs():
    visited = [(0, 0)]
    queue = deque([(0, 0)])

    while queue:
        (x, y) = queue.popleft()
        for (dx, dy) in dirs:
            nextx = x + dx
            nexty = y + dy

            if nextx < 0 or nexty < 0 or nextx >= len(board) or nexty >= len(board):
                continue

            if (nextx, nexty) not in visited:
                visited.append((nextx, nexty))
                print("({}, {})".format(nextx, nexty))
                queue.append((nextx, nexty))


if __name__ == "__main__":
    print("--- dfs ---")
    dfs()
    print("--- bfs ---")
    bfs()
