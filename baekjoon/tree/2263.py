from .. import util

example = """
3
1 2 3
1 3 2
"""
util.setinput(example)

"""
Ref: https://suhwanc.tistory.com/26

(!)
Python의 기본 recursion limit은 1000으로 (sys.getrecursionlimit())
설정되어있어 재귀를 사용할 때 이를 초과할 것 같다면 sys.setrecursionlimit(limit)을
통해 늘려줘야 RecursionError를 방지할 수 있다.

(https://docs.python.org/3/library/exceptions.html#RecursionError)
"""
import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

index = [0 for _ in range(n + 1)]
for idx in range(n):
    index[in_order[idx]] = idx


def pre_order(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = post_order[post_end]
    root_idx = index[root]

    left = root_idx - in_start

    print(root, end=" ")
    pre_order(in_start, root_idx - 1, post_start, post_start + left - 1)
    pre_order(root_idx + 1, in_end, post_start + left, post_end - 1)


pre_order(0, n - 1, 0, n - 1)