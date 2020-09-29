from .. import util

example = """
1
"""
util.setinput(example)

# Hint: https://www.acmicpc.net/board/view/54580
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]


def bfs(start):
    visited = [0 for _ in range(N + 1)]
    visited[start] = 1
    queue = deque([(start, 0)])

    longest_length = 0
    longest_node = 0

    while queue:
        current, length = queue.popleft()

        is_leaf = True
        for child, weight in tree[current]:
            if not visited[child]:
                is_leaf = False
                visited[child] = 1
                queue.append((child, length + weight))

        if is_leaf:
            if length > longest_length:
                longest_length = length
                longest_node = current

    return (longest_node, longest_length)


for _ in range(N - 1):
    s, e, w = map(int, input().split())
    tree[s].append((e, w))
    tree[e].append((s, w))

longest_from_root = bfs(1)
longest_from_leaf = bfs(longest_from_root[0])
print(longest_from_leaf[1])
