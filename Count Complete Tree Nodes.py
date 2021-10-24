# Qus:https://leetcode.com/problems/count-complete-tree-nodes/

# time complexity : o(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def nodesInTree(root):
    
    
    if(root==None):
        return 0
    a = 0
    b = 0 
    if(root.left):
        a = nodesInTree(root.left)
    if(root.right):
        b = nodesInTree(root.right)
    return 1 + a + b
        



class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return nodesInTree(root)


# optimal solution O(log(n)*log(n))
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        



class Solution(object):
    def countNodes(self, root,d={}):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root==None):
            return 0
        
        leftDepth = self.getDepth(root.left,True,d)
        rightDepth = self.getDepth(root.right,False,d)
        
        if(leftDepth==rightDepth):
            return 2**(leftDepth+1)-1
        
        return 1 + self.countNodes(root.left,d) + self.countNodes(root.right,d)
        
        
        
        
    
    def getDepth(self,root,isLeft,d):
    
        if(root==None):
            return 0
        if(d.get((root,isLeft),False)!=False):
            return d.get((root,isLeft),False)
        
        if(isLeft):
            d[(root,isLeft)] = 1 + self.getDepth(root.left,isLeft,d)
            return d[(root,isLeft)]
        d[(root,isLeft)] = 1 + self.getDepth(root.right,isLeft,d)
        return d[(root,isLeft)]


# without memo is more efficient
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        



class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root==None):
            return 0
        
        
        leftDepth = self.getDepth(root.left,True)
        rightDepth = self.getDepth(root.right,False)
        
        if(leftDepth==rightDepth):
            return 2**(leftDepth+1)-1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        

    def getDepth(self,root,isLeft):
    
        if(root==None):
            return 0
        
        if(isLeft):
            return 1 + self.getDepth(root.left,isLeft)
        return 1 + self.getDepth(root.right,isLeft)
            
