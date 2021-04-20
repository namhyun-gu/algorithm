import io
import sys

example = """
6
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import collections


def bfs():
    queue = collections.deque()
    queue.append((1, 0, 0))

    visit = [[0 for _ in range(1001)] for _ in range(S + 1)]
    visit[1][0] = 1

    while queue:
        cur, clipboard, cnt = queue.popleft()

        if cur == S:
            return cnt

        if clipboard:
            if cur + clipboard <= S:
                if not visit[cur + clipboard][clipboard]:
                    visit[cur + clipboard][clipboard] = 1
                    queue.append((cur + clipboard, clipboard, cnt + 1))

        if not visit[cur][cur]:
            visit[cur][cur] = 1
            queue.append((cur, cur, cnt + 1))

        if cur - 1 >= 0:
            if not visit[cur - 1][clipboard]:
                visit[cur - 1][clipboard] = 1
                queue.append((cur - 1, clipboard, cnt + 1))
    return 0


if __name__ == "__main__":
    input = sys.stdin.readline

    S = int(input())
    ret = bfs()
    print(ret)
