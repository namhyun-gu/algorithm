import io
import sys

example = """
4
0 0
0 10
10 10
10 0
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys

# Ref: https://velog.io/@skyepodium/%EB%B0%B1%EC%A4%80-2166-%EB%8B%A4%EA%B0%81%ED%98%95%EC%9D%98-%EB%A9%B4%EC%A0%81
def ccw(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c

    return (bx - ax) * (cy - ay) - (cx - ax) * (by - ay)


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    coords = []
    for _ in range(N):
        x, y = map(int, input().split())
        coords.append((x, y))

    result = 0
    for i in range(1, len(coords) - 1):
        result += ccw(coords[0], coords[i], coords[i + 1])

    print(abs(result) / 2)