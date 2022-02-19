# Qus:https://leetcode.com/problems/insert-delete-getrandom-o1/

#inefficient solution
import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d={}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if(val in self.d):
            return False
        self.d[val]=True
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if(val in self.d):
            del self.d[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        rand=random.randint(0,len(self.d.keys())-1)
        # print rand,self.d.keys()
        return self.d.keys()[rand]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



# efficient approach using swap with last element on deletion
import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d={}
        self.keys=[]

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if(val in self.d):
            return False
        self.d[val]=len(self.keys)
        self.keys.append(val)
        
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if(val in self.d):
            
            #delete elemnt at this index
            index=self.d[val]
            #swap last element with this index
            self.keys[index],self.keys[-1]=self.keys[-1],self.keys[index]
            #handle case when val is at last position
            self.d[self.keys[index]]=index
            #pop out last element
            self.keys.pop()

            del self.d[val]
            return True
        
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        rand=random.randint(0,len(self.keys)-1)
        # print rand,self.d.keys()
        return self.keys[rand]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

