# %%
def union(parents, a, b):
    # a, b의 부모에 대한 정보를 찾고
    # 부모가 같지 않다면 찾은 b의 부모 값에 a의 부모 값을 저장한다.
    # 이 과정을 통해 a와 b는 같은 부모를 갖는 집합에 속한다. (Union)
    a_parent = find(parents, a)
    b_parent = find(parents, b)

    if a_parent == b_parent:
        return

    parents[b_parent] = a_parent


def find(parents, x):
    # 부모를 찾으려는 x의 값과 x의 부모가 같다면 그대로 반환한다.
    # (부모에 대한 정보를 갖지 않음)
    if x == parents[x]:
        return x

    # x의 부모 값으로 상위 부모에 대한 정보를 찾아 x의 부모에 저장한다.
    parents[x] = find(parents, parents[x])
    return parents[x]


graph = [[1, 2], [2, 3], [4, 5]]

# 부모에 대한 정보를 담은 배열을 저장한다.
# 초기화 시 자기 자신의 값으로 저장한다.
parents = [i for i in range(6)]

for parent, child in graph:
    union(parents, parent, child)

parents