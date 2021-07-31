from random import choice, randint
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.random_set = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        val_in_set = val in self.random_set
        self.random_set.add(val)
        return not val_in_set

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        val_in_set = val in self.random_set
        if val_in_set:
            self.random_set.remove(val)
        return val_in_set

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        rand_element = choice(tuple(self.random_set))
        return rand_element


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()