import io
import sys

example = """
4 6
a t c i s w
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

L, C = map(int, input().split())
alphabets = sorted(input().split())
vowels = set(["a", "e", "i", "o", "u"])
temp = ["" for _ in range(C)]


def can_key(key: str) -> bool:
    vowel = 0
    not_vowel = 0
    for c in key:
        if c in vowels:
            vowel += 1
        else:
            not_vowel += 1

        if vowel >= 1 and not_vowel >= 2:
            return True
    return False


def permutations(idx, depth):
    global temp

    if depth == L:
        key = "".join(temp)
        if can_key(key):
            print(key)
        return

    for i in range(idx, len(alphabets)):
        temp[depth] = alphabets[i]
        permutations(i + 1, depth + 1)


permutations(0, 0)