# QUs:https://leetcode.com/problems/sum-of-left-leaves/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def sumleaf(root):
    if(root==None ):
        return 0
    
    #incase current node is leaf node return val of current node
    if(root.left==None and root.right==None):
        return root.val
    
    a,b=0,0
    #go to left side until left root is not reached
    if(root.left):
        a=sumleaf(root.left)
    #dont go to right side if right node is  a root node 
    #else go to right side may be its left side is a leaf node
    if(root.right and (root.right.left!=None or root.right.right!=None )):
        b=sumleaf(root.right)
        
#     return sum of leaf from right node and left node
    return a+b


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #since root is not the leaf node 
        #so it is a special case
        if(root==None or (root.left==None and root.right==None)):
            return 0
        return sumleaf(root)