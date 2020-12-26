class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if stack:
                    top = stack[-1]
                    if (
                        (top == "(" and c == ")")
                        or (top == "{" and c == "}")
                        or (top == "[" and c == "]")
                    ):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return not stack


if __name__ == "__main__":
    sol = Solution()

    print(sol.isValid("()"))  # Expect True
    print(sol.isValid("()[]{}"))  # Expect True
    print(sol.isValid("(]"))  # Expect False
    print(sol.isValid("([]])"))  # Expect False
    print(sol.isValid("{[]}"))  # Expect True
    print(sol.isValid("(])"))  # Expect False
