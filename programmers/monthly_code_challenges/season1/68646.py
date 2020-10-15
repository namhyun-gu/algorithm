"""
문제를 어떻게 접근해야할지 몰라서 문제 내 질문하기에 있는 힌트를 참고했다

Ref: https://programmers.co.kr/questions/13657

터트릴 수 있는 풍선은
풍선 위치를 기준으로 왼쪽과 오른쪽 최소값 중에 한번이라도 작으면 답에 들어가고
두 최소값보다 크다면 답에 들어갈 수 없다.

최소값을 구하는 방법은
풍선 위치를 기준으로 슬라이스해서 구하는 방법이 있지만
이 방법대로 구하게 되면 시간초과가 나오게 된다.

왼쪽 풍선부터 오른쪽까지 최소값을 각 위치별 배열에 저장하고
같은 방법으로 반대 방향을 구한 뒤

모든 풍선을 확인하며 두 최소값을 비교하고, 정답을 더하면 구할 수 있다.
"""

MAX = 1_000_000_001


def solution(a):
    answer = 0
    left, right = MAX, MAX
    map = [[0, 0] for _ in range(len(a))]
    for idx in range(len(a)):
        left = min(left, a[idx])
        map[idx][0] = left

    for idx in reversed(range(len(a))):
        right = min(right, a[idx])
        map[idx][1] = right

    for idx in range(len(a)):
        if a[idx] <= map[idx][0] or a[idx] <= map[idx][1]:
            answer += 1
    return answer


if __name__ == "__main__":
    assert solution([9, -1, -5]) == 3
    assert solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]) == 6
