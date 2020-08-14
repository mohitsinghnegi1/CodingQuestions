# Qus:https://leetcode.com/problems/flatten-nested-list-iterator/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
def getAll(nestedList,q):
    
    # print nestedList
    # here i is a nestedInteger which have 3 functions isInteger(), getInteger(), getList()
    # getList() will return a list of Nestednumber
    for i in nestedList:
        if(i.isInteger()):
            q.append(i.getInteger())
            # print q
        else:
            getAll(i.getList(),q)

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        #q will hold all the destructured elements
        self.q=[]
        
        # this method will get all the integer value inside this nestedList type                       # List[NestedInteger]
        getAll(nestedList,self.q)
        
        #doing reverse to get next element faster
        self.q.reverse()

    def next(self):
        """
        :rtype: int
        """
        return self.q.pop() if self.q else -1
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q)>0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())