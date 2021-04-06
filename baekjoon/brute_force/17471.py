import io
import sys

example = """
6
5 2 3 4 1 2
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import collections


def get_group(graph, start, n, exclude=set()):
    queue = collections.deque()
    queue.append(start)

    visit = set()

    while queue:
        cur = queue.popleft()
        visit.add(cur)
        if n != -1 and len(visit) == n:
            break

        for next in graph[cur]:
            if next not in visit and next not in exclude:
                queue.append(next)

    return visit


def is_connect(graph, group):
    start = list(group)[0]

    queue = collections.deque()
    queue.append(start)
    visit = set()
    visit.add(start)

    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if next not in visit and next in group:
                visit.add(next)
                queue.append(next)

    return len(visit) == len(group)


def group_city(n, include=set()):
    global min_diff

    if n == N + 1:
        a_group = include
        b_group = set(range(1, N + 1)).difference(a_group)

        if len(a_group) in range(1, N) and len(b_group) in range(1, N):
            if is_connect(graph, a_group) and is_connect(graph, b_group):
                diff = abs(cal_populate(a_group) - cal_populate(b_group))
                min_diff = min(min_diff, diff)
        return

    include.add(n)
    group_city(n + 1)
    include.remove(n)
    group_city(n + 1)


def cal_populate(group):
    ret = 0
    for city in group:
        ret += populate[city]
    return ret


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    populate = [0, *map(int, input().split())]
    graph = [[] for _ in range(N + 1)]

    for n in range(1, N + 1):
        _, *near = map(int, input().split())
        graph[n] = near

    min_diff = sys.maxsize

    group_city(1)

    print(min_diff if min_diff != sys.maxsize else -1)