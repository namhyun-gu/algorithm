import unittest

"""
이 문제를 처음 접근할때 백준에서 숨바꼭질 문제가 이와 비슷하여
0-1 BFS를 통해 제출하였으나, 시간초과가 발생하고, 효율성 테스트에서 통과하지 못 했다.

BFS를 통한 접근 방법에 문제가 있는 것 같아 검색해보니
백준의 숨바꼭질 문제는 이전으로 돌아가는 경우도 있기에 BFS를 활용해야하나
이 문제의 경우 계속 앞으로 가기만 하면 된다.

비용이 들지 않는 순간이동을 최대한 많이 하면 되는데

0 에서 5로 이동을 할때
0 > 1(+1) > 2(+0) > 4(+0) > 5 (+1) 로 이동하는 것을

반대로 생각하여 다음과 같이 이동한다고 생각하면
5 > 4 > 2 > 1 > 0

홀수일때, 점프를 사용하여 -1로 이동,
짝수일때, 순간이동으로 2를 나눈 자리로 이동하면 된다.
"""


def solution(n):
    cost = 0
    while n > 0:
        if n % 2 == 0:
            n /= 2
        else:
            cost += 1
            n -= 1
    return cost


class SolutionTest(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution(5), 2)

    def test_example_2(self):
        self.assertEqual(solution(6), 2)

    def test_example_3(self):
        self.assertEqual(solution(5000), 5)


if __name__ == "__main__":
    unittest.main(verbosity=True)