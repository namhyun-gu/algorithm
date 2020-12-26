from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                elif token == "/":
                    stack.append(int(left / right))
            else:
                stack.append(int(token))
        return stack.pop()


if __name__ == "__main__":
    sol = Solution()

    ret = sol.evalRPN(["2", "1", "+", "3", "*"])
    print(ret)  # Expect 9

    ret = sol.evalRPN(["4", "13", "5", "/", "+"])
    print(ret)  # Expect 6

    ret = sol.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
    print(ret)  # Expect 22

    ret = sol.evalRPN(["4", "-2", "/", "2", "-3", "-", "-"])
    print(ret)  # Expect -7
