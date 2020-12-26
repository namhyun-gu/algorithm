class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        ret = ""
        if numerator / denominator < 0:
            ret += "-"

        numerator = abs(numerator)
        denominator = abs(denominator)

        ret += str(numerator // denominator)
        numerator %= denominator

        if numerator == 0:
            return ret

        ret += "."
        map = dict()

        while numerator > 0:
            if numerator in map:
                idx = map[numerator]
                ret = ret[:idx] + "(" + ret[idx:] + ")"
                break
            else:
                map[numerator] = len(ret)

            numerator *= 10
            ret += str(numerator // denominator)
            numerator %= denominator

        return ret


if __name__ == "__main__":
    sol = Solution()

    ret = sol.fractionToDecimal(numerator=1, denominator=2)
    print(ret)  # Expected "0.5"

    ret = sol.fractionToDecimal(numerator=2, denominator=1)
    print(ret)  # Expected "2"

    ret = sol.fractionToDecimal(numerator=2, denominator=3)
    print(ret)  # Expected "0.(6)"

    ret = sol.fractionToDecimal(numerator=4, denominator=333)
    print(ret)  # Expected "0.(012)"

    ret = sol.fractionToDecimal(numerator=1, denominator=5)
    print(ret)  # Expected "0.2"

    ret = sol.fractionToDecimal(numerator=-50, denominator=8)
    print(ret)  # Expected "-6.25"
