from .. import util

example = """
12 16
ABCDEFGHIJKLMNOP
BCDEFGHIJKLMNOPQ
CDEFGHIJKLMNOPQR
DEFGHIJKLMNOPQRS
EFGHIJKLMNOPQRST
FGHIJKLMNOPQRSTU
GHIJKLMNOPQRSTUV
HIJKLMNOPQRSTUVW
IJKLMNOPQRSTUVWX
JKLMNOPQRSTUVWXY
KLMNOPQRSTUVWXYZ
LMNOPQRSTUVWXYZA
"""
util.setinput(example)

"""
이 문제를 처음 풀 때 visited 배열을 2차원으로 만들어서
구현을 시도해보았으나 visited를 체크해야 하는 위치를 선정하는 것이 생각이 나지 않았고
dfs 시작 처음에 무조건 조건문을 넣고 리턴을 해야한다는 고정관념이 있어서 해결방법을
떠올리는 데 어려웠다.

검색을 통해 visited 에는 알파벳 방문 여부만 넣으면 된다는 걸 알 수 있었으며
조건문을 넣지 않고 매 dfs마다 최대 depth을 갱신하면 된다는 걸 알 수 있었다.

기본 예제가 해결되고 제출을 하니 시간초과가 발생하였는데
visited 배열 대신 O(1) 연산을 수행할 수 있는 Set, Dictionary로 해도 시간초과가 발생했는데
이 또한 검색해보니 pypy3로 제출하면 된다고 하던데도 시간초과가 발생했다.

검색을 통해 보드 배열을 생성할 떄 알파벳을 숫자로 변환한 값을 넣고,
그 값을 visited 배열에서 활용하도록 한 뒤, pypy3로 제출을 하니 통과가 되었다.

자바나 C++로 문제를 풀 땐 큰 수를 처리하거나 알고리즘을 잘못 생각해서 해결을 못 했는데
파이썬에서는 맞는 알고리즘을 쓰더라도 느려서 시간초과가 발생하는 경우가 많은데
PyPy3로 제출을 하면 해결이 되는 경우도 있었지만, 이번처럼 세부적인 최적화를 해야 통과가 된다는 점이 어려운 것 같다.
"""
import sys

input = sys.stdin.readline
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
max_depth = 0

R, C = map(int, input().split())
board = []
visited = [0 for _ in range(26)]

for r in range(R):
    board.append(list(map(lambda x: ord(x) - 65, input())))


def is_valid(r, c):
    return 0 <= r < R and 0 <= c < C


def dfs(r, c, depth):
    global max_depth
    max_depth = max(max_depth, depth)

    for dr, dc in dirs:
        tr = r + dr
        tc = c + dc

        if is_valid(tr, tc) and not visited[board[tr][tc]]:
            visited[board[tr][tc]] = 1
            dfs(tr, tc, depth + 1)
            visited[board[tr][tc]] = 0


visited[board[0][0]] = 1
dfs(0, 0, 1)
print(max_depth)