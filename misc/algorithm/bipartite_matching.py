#
# Bipartite Matching
#
# Ref: https://www.crocus.co.kr/499

MAX_N = 201
MAX_M = 201

# adj[i][j] = Ai와 Bj가 연결되어 있는가?
adj = [[False for _ in range(MAX_M)] for _ in range(MAX_N)]

visited = set()

n, m = 4, 4  # A와 B 정점 수
a_match, b_match = [-1] * n, [-1] * m


def dfs(a: int) -> bool:
    if a in visited:
        return False

    visited.add(a)

    for b in range(m):
        if adj[a][b]:
            # B가 매칭되어 있지 않다면 (-1),
            # b_match[b]부터 시작해 증가 경로를 찾는다.
            # 매칭되어 있다면 dfs에서 매칭되어있는 A 정점이 다른 곳을 매칭할 수 있는지 본다.
            if b_match[b] == -1 or dfs(b_match[b]):
                # 증가 경로를 발견하였을 떄, a와 b를 매치시킨다. (= 이어준다)
                a_match[a] = b
                b_match[b] = a
                return True
    return False


def bipartite_match():
    global visited

    size = 0
    for start in range(n):
        visited = set()
        if dfs(start):
            size += 1
    return size


if __name__ == "__main__":
    # A의 정점 i와 B의 정점 j가 연결되어 있다면 1로 표시
    adj[0][0] = 1
    adj[0][1] = 1
    adj[0][3] = 1

    adj[1][0] = 1
    adj[1][1] = 1

    adj[2][0] = 1
    adj[2][2] = 1

    adj[3][2] = 1
    adj[3][3] = 1

    print(bipartite_match())