class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            number = self.countAndSay(n - 1)
            say = ""

            prev = number[0]
            cnt = 1
            for idx in range(1, len(number)):
                if prev != number[idx]:
                    say += str(cnt) + prev
                    prev = number[idx]
                    cnt = 1
                else:
                    cnt += 1
            say += str(cnt) + prev
            return say


if __name__ == "__main__":
    sol = Solution()
    ret = sol.countAndSay(2)
    print(ret)

    ret = sol.countAndSay(3)
    print(ret)

    ret = sol.countAndSay(4)
    print(ret)  # Expect 1211

    ret = sol.countAndSay(5)
    print(ret)  # Expected 111221

    ret = sol.countAndSay(6)
    print(ret)  # Expected 312211
