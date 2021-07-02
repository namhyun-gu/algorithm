# region Input redirection
import io
import sys

example = """
9999
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys


def fill(numbers):
    for n in range(10):
        n = str(n)
        numbers.setdefault(n, 0)
        numbers[n] += 1


if __name__ == "__main__":
    input = sys.stdin.readline

    N = input().rstrip()
    answer = 1

    numbers = dict()
    fill(numbers)

    for n in N:
        if n not in ["6", "9"]:
            if numbers[n] == 0:
                answer += 1
                fill(numbers)
            numbers[n] -= 1
        else:
            if numbers[n] == 0:
                if n == "6" and numbers["9"] > 0:
                    numbers["9"] -= 1
                elif n == "9" and numbers["6"] > 0:
                    numbers["6"] -= 1
                else:
                    answer += 1
                    fill(numbers)
                    numbers[n] -= 1
            else:
                numbers[n] -= 1

    print(answer)