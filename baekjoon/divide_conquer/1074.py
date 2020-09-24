from .. import util

example = """
15 0 0
"""
util.setinput(example)

import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())


def contain_area(area_r, area_c, n):
    return area_r <= r and r < area_r + n \
        and area_c <= c and c < area_c + n


def visit(cur_r, cur_c, n, idx):
    if n == 1:
        if cur_r == r and cur_c == c:
            print(idx)
            exit(0)
        return idx + 1
    else:
        half = int(n / 2)
        areas = [
            (cur_r, cur_c),
            (cur_r, cur_c + half),
            (cur_r + half, cur_c),
            (cur_r + half, cur_c + half),
        ]

        cur_idx = idx
        for area_r, area_c in areas:
            if not contain_area(area_r, area_c, half):
                cur_idx += half ** 2
            else:
                cur_idx += visit(area_r, area_c, half, cur_idx)


visit(0, 0, 2 ** N, 0)
