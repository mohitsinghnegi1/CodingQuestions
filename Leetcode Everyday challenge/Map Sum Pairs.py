# Qus:https://leetcode.com/problems/map-sum-pairs/

# Time complexity : O(k) where k is the length of string
# space is linear

class Node:

    def __init__(self):
        self.childrens = {}
        self.end = 0


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word, val):
        par = self.root

        for char in word:
            if(char not in par.childrens):
                par.childrens[char] = Node()
            par = par.childrens[char]
        par.end = val

    def getWordsWithPrefix(self, prefix):
        par = self.root

        for char in prefix:
            if(char not in par.childrens):
                return None

            par = par.childrens[char]

        return par


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.trie.insert(key, val)

    def getVal(self, childrens):

        total = 0
        # print childrens.keys()
        for char in childrens:
            # print char
            node = childrens[char]
            # print "==> ",node,node.val
            total += node.end
            total += self.getVal(node.childrens)

        return total

    def getSum(self, prev):

        # get sum of all childrens which contains this prefix
        return prev.end + self.getVal(prev.childrens)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        prev = self.trie.getWordsWithPrefix(prefix)
        if(prev):
            return self.getSum(prev)
        return 0


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
