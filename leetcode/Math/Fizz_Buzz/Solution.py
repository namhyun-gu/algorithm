from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            string = ""
            if i % 3 == 0 or i % 5 == 0:
                if i % 3 == 0:
                    string += "Fizz"
                if i % 5 == 0:
                    string += "Buzz"
            else:
                string += str(i)
            result.append(string)
        return result