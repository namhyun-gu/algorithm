import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.data:
            self.data.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data:
            self.data.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(list(self.data))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == "__main__":
    randomizedSet = RandomizedSet()

    print(randomizedSet.insert(1))  # Expect true
    print(randomizedSet.remove(2))  # Expect false
    print(randomizedSet.insert(2))  # Expect true
    print(randomizedSet.getRandom())  # Expect 2
    print(randomizedSet.remove(1))  # Expect true
    print(randomizedSet.insert(2))  # Expect false
    print(randomizedSet.getRandom())  # Expect 2
