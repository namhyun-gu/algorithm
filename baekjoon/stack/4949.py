import io
import sys

example = """
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
).
.
"""
sys.stdin = io.StringIO(example.strip())

import sys

input = sys.stdin.readline

while True:
    line = input()
    if line == ".\n" or line == ".":
        break

    stack = []

    for c in line:
        if c == "(" or c == "[":
            stack.append(c)
        else:
            if c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(c)
            elif c == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(c)

    if stack:
        print("no")
    else:
        print("yes")
