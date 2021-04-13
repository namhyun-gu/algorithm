import io
import sys

example = """
4
50 50 0 10
50 50 1 10
50 50 2 10
50 50 3 10
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys

dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def rotate(dir):
    return (dir + 1) % 4


def cal_dragon_curve(paper):
    curve = 0
    for y in range(100):
        for x in range(100):
            if (
                paper[y][x]
                and paper[y][x + 1]
                and paper[y + 1][x]
                and paper[y + 1][x + 1]
            ):
                curve += 1
    return curve


def make_pattern(pattern):
    size = len(pattern)
    for i in reversed(range(0, size)):
        dir = rotate(pattern[i])
        pattern.append(dir)


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())

    paper = [[0 for _ in range(101)] for _ in range(101)]

    for _ in range(N):
        x, y, dir, gen = map(int, input().split())

        pattern = [dir]
        for g in range(gen):
            make_pattern(pattern)

        paper[y][x] = 1
        for p in pattern:
            dx, dy = dirs[p]
            x, y = x + dx, y + dy
            paper[y][x] = 1

    print(cal_dragon_curve(paper))