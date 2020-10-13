from .. import util

example = """
3 2
1 1
2 2 3
2 1 2
"""
util.setinput(example)

"""
Union-Find

Ref: https://ko.wikipedia.org/wiki/서로소_집합_자료_구조
Ref (2): https://yabmoons.tistory.com/463

이 문제는 단순히 파티 순서대로 진실을 아는 사람이 있는지 확인하고 있다면
해당 파티는 과장을 못한다고 판단하여 파티 수를 계산하였는데 이 방식으로는


"어떤 사람이 어떤 파티에서는 진실을 듣고,
또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다."

조건을 만족할 수 없다. Union-Find 알고리즘를 이용하여
각 사람들이 어떤 사람에 연결되는지를 Union 연산으로 구한 후, (각 파티 별 첫번째 사람이 루트)

각 파티의 참석자들과 진실을 아는 사람을 Find 연산으로 같은 부모를 갖는지 확인한다.
같은 부모를 갖는다면 해당 파티 참석자는 진실을 알고 있는 것이므로
해당 파티는 과장되게 말할 수 없음을 알아낼 수 있다.
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
parties = []
_, *knows = map(int, input().split())


def find(x):
    if x == parent[x]:
        return x
    return find(parent[x])


def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return

    parent[x_root] = y_root


for m in range(M):
    _, *participate = map(int, input().split())
    parties.append(participate)
    root = participate[0]
    for idx in range(1, len(participate)):
        union(root, participate[idx])


cnt = 0
for party in parties:
    can_over = True

    for num in party:
        for know in knows:
            if find(num) == find(know):
                can_over = False
                break
    if can_over:
        cnt += 1

print(cnt)