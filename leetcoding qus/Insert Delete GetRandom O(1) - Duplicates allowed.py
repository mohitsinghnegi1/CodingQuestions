# QUs:https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
from collections import defaultdict
import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(set)  # will contain val as key and index as value
        self.keys = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        # if element not in d simply insert it and return true
        # add index in d
        if(val not in self.d):
            self.d[val].add(len(self.keys))
            self.keys.append(val)
            return True
        self.d[val].add(len(self.keys))
        self.keys.append(val)

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if(val not in self.d):
            return False

       # if cur is the last element then
        if(len(self.d[val]) == 1):

            idx = self.d[val].pop()  # index of element
            # swap with the last element
            self.keys[idx], self.keys[-1] = self.keys[-1], self.keys[idx]
            # now last element present in idx pos

            # if the element not present at the end the update the index of val
            if(idx != len(self.keys)-1):
                lstPosIndex = len(self.keys)-1
                elSwapped = self.keys[idx]

                self.d[elSwapped].discard(lstPosIndex)
                self.d[elSwapped].add(idx)

            self.keys.pop()
            # delete the entry from d
            del self.d[val]
            return True

        # in case there are multiple elements having same value

        # pop one of the index
        # remove element from the dict set as we have more element
        idx = self.d[val].pop()
        # swap with last element
        self.keys[idx], self.keys[-1] = self.keys[-1], self.keys[idx]

        # if not at end pos then update the swapped elemnt idx
        if(idx != len(self.keys)-1):
            lstPosIndex = len(self.keys)-1
            elSwapped = self.keys[idx]

            self.d[elSwapped].discard(lstPosIndex)
            self.d[elSwapped].add(idx)

        self.keys.pop()

        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        # get random element from the list
        return self.keys[random.randint(0, len(self.keys)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
