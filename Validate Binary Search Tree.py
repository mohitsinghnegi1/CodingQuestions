# QUs:https://docs.google.com/spreadsheets/d/1qS2-2AHpFoiw8ar6LuN9R5hVu79-bIGj-8c1BeCB9wg/edit#gid=0
# there are two ways to solve this qus
# 1 using inorder (LRootR) traversal
# 2nd using min or max limit




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
def isBST(root,min1,max1):
    
        if(root==None):
            return True
        # check if cur node is valid not (ie comes in the given range or not)
        if not (root.val<max1 and root.val>min1):
            return False
        # all nodes should be valid BST
        return isBST(root.left,min1,root.val) and isBST(root.right,root.val,max1)
            

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return isBST(root,-sys.maxsize,sys.maxsize)