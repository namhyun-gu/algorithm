from .. import util

example = """
ABC ABCDAB ABCDABCDABDE
ABCDABD
"""
util.setinput(example)

"""
KMP algorithm

Ref: https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
Ref (2): https://algorithm-visualizer.org/dynamic-programming/knuth-morris-pratts-string-search
"""
import sys

input = sys.stdin.readline

T = input().rstrip()
P = input().rstrip()


def get_kmp_table(pattern):
    table = [0 for _ in range(len(pattern))]

    postfix = 1
    prefix = 0

    while postfix < len(pattern):
        while prefix > 0 and pattern[postfix] != pattern[prefix]:
            prefix = table[prefix - 1]

        if pattern[postfix] == pattern[prefix]:
            prefix += 1

        table[postfix] = prefix
        postfix += 1

    return table


def kmp(string, pattern):
    position = []
    table = get_kmp_table(pattern)

    i = 0
    k = 0
    while i < len(string):
        while k > 0 and string[i] != pattern[k]:
            k = table[k - 1]

        if string[i] == pattern[k]:
            k += 1
            if k == len(pattern):
                position.append(i - len(pattern) + 1)
                k = table[k - 1]
        i += 1
    return position


positions = kmp(T, P)
print(len(positions))
for position in positions:
    print(position + 1, end=" ")