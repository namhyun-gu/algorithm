from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ret = []
        self.generate(n)
        return self.ret

    def generate(self, n: int, parenthesis: List[str] = []):
        if len(parenthesis) == n * 2:
            if self.valid_parenthesis(parenthesis):
                self.ret.append("".join(parenthesis))
        else:
            parenthesis.append("(")
            self.generate(n, parenthesis)
            parenthesis.pop()
            parenthesis.append(")")
            self.generate(n, parenthesis)
            parenthesis.pop()

    def valid_parenthesis(self, parenthesis: List[str]) -> bool:
        stack: List[str] = []
        for p in parenthesis:
            if p == "(":
                stack.append(p)
            else:
                if len(stack) and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(p)
        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()

    ret = sol.generateParenthesis(3)
    print(ret)

    ret = sol.generateParenthesis(1)
    print(ret)

    ret = sol.generateParenthesis(8)
    print(ret)