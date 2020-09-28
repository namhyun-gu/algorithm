from .. import util

example = """
4
1234 3412
1000 1
1 16
9998 9999
"""
util.setinput(example)

import sys
from collections import deque
input = sys.stdin.readline


def do_s(n):
    if n == 0:
        return 9999
    return n - 1


def do_l(n):
    first = int(n / 1000)
    n -= first * 1000
    n *= 10
    n += first
    return int(n)


def do_r(n):
    end = n % 10
    n -= end
    n /= 10
    n += end * 1000
    return int(n)


operations = {
    'D': lambda n: (n * 2) % 10000,
    'S': do_s,
    'L': do_l,
    'R': do_r
}


def bfs(start, end):
    queue = deque([(start, "")])
    visited = [0 for _ in range(10000)]
    visited[start] = 1

    while queue:
        current, operation = queue.popleft()
        if current == end:
            return operation

        for oper in operations:
            func = operations[oper]
            result = func(current)
            if not visited[result]:
                visited[result] = 1
                queue.append((result, operation + oper))
    return ""


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    operation = bfs(A, B)
    print(operation)
