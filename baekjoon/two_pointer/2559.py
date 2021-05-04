# region Input redirection
import io
import sys

example = """
10 5
3 -2 -4 -9 0 3 7 13 8 -3
"""
sys.stdin = io.StringIO(example.strip())
# endregion
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    N, K = map(int, input().split())
    nums = [0]

    for idx, num in enumerate(map(int, input().split())):
        idx += 1
        nums.append(num)
        nums[idx] += nums[idx - 1]

    ret = -sys.maxsize

    for i in range(N - K + 1):
        sum = nums[i + K] - nums[i]
        ret = max(ret, sum)

    print(ret)