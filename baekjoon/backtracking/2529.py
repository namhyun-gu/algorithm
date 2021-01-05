import io
import sys

example = """
2
< > 
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

K = int(input())
signs = input().split()

maximum, minimum = None, None


def is_valid(picks):
    if len(picks) < 2:
        return True

    for i in range(len(picks) - 1):
        if signs[i] == "<" and not (picks[i] < picks[i + 1]):
            return False
        elif signs[i] == ">" and not (picks[i] > picks[i + 1]):
            return False
    return True


def backtracking(picks=[], nums=set()):
    global maximum, minimum

    if len(picks) == K + 1:
        num = "".join(map(str, picks))
        maximum = max(maximum, num) if maximum else num
        minimum = min(minimum, num) if minimum else num
        return

    for n in range(10):
        if n not in nums:
            nums.add(n)
            picks.append(n)

            if is_valid(picks):
                backtracking(picks[:], set(nums))

            nums.remove(n)
            picks.pop()


backtracking()
print(maximum, minimum, sep="\n")