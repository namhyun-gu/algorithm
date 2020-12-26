class Solution:
    def isHappy(self, n: int) -> bool:
        num_set = set()
        stack = [n]
        ret = False
        while stack:
            cur = stack.pop()
            num_str = str(cur)
            num_sum = sum(map(lambda i: int(i) ** 2, num_str))

            if num_sum == 1:
                ret = True
            else:
                if num_sum not in num_set:
                    num_set.add(num_sum)
                    stack.append(num_sum)
                else:
                    ret = False
                    break
        return ret


if __name__ == "__main__":
    sol = Solution()

    ret = sol.isHappy(19)
    print(ret)  # Expect True

    ret = sol.isHappy(2)
    print(ret)
