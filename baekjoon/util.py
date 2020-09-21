from io import StringIO
import sys


def setinput(input: str):
    sys.stdin = StringIO(input.strip())
