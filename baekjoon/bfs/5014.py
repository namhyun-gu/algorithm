# region Input redirection
import io
import sys

example = """
100 2 1 1 0
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import collections


def bfs(building, src, dest, u, d):
    queue = collections.deque()
    queue.append(src)

    building[src] = 1

    while queue:
        cur = queue.popleft()

        if cur == dest:
            return building[dest] - 1

        for next in [u, -d]:
            if cur + next in range(1, F + 1):
                if building[cur + next] == 0:
                    building[cur + next] = building[cur] + 1
                    queue.append(cur + next)

    return -1


if __name__ == "__main__":
    input = sys.stdin.readline

    F, S, G, U, D = map(int, input().split())

    building = [0] * (F + 1)

    ret = bfs(building, S, G, U, D)

    if ret != -1:
        print(ret)
    else:
        print("use the stairs")