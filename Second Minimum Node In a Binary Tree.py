# Qus:https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys

class Solution(object):
    
    def __init__(self):
        self.ans = sys.maxsize
    
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = sys.maxsize
        min1 = root.val
        
        def secondMin(root):
            
            if(root==None):
                return 
            
            if(min1<root.val<self.ans):
                self.ans = root.val
            elif(root.val==min1):
                
                secondMin(root.left)
                secondMin(root.right)
            
            

        secondMin(root)
        
        return self.ans if self.ans!=sys.maxsize else -1
            
            