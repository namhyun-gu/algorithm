import io
import sys

example = """
3
1 3
2 4
3 5
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys
import heapq

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())

    max_t = 0
    heap = []
    room = []

    for _ in range(N):
        s, t = map(int, input().split())
        heapq.heappush(heap, (s, t))

    while heap:
        s, t = heapq.heappop(heap)

        if not room:
            heapq.heappush(room, t)
        else:
            if s >= room[0]:
                heapq.heappop(room)
            heapq.heappush(room, t)

    print(len(room))