import io
import sys

example = """
7 50
1 12 5 111 200 1000 10
"""
sys.stdin = io.StringIO(example.strip())
#
# ⛔ DO NOT COPY ABOVE CONTENTS
#
def maximumToys(prices, k):
    prices = sorted(prices)
    
    count = 0

    for price in prices:
        if price <= k:
            k -= price
            count += 1
        else:
            break

    return count

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(result)