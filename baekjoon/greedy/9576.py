import io
import sys

example = """
1
2 3
1 2
1 2
1 2
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    book = [False] * (N + 1)
    students = []
    for _ in range(M):
        a, b = map(int, input().split())
        students.append((b, a))
    students.sort()

    cnt = 0
    for student in students:
        b, a = student
        for n in range(a, b + 1):
            if not book[n]:
                book[n] = True
                cnt += 1
                break

    print(cnt)
