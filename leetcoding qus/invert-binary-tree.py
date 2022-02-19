# QUs:https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invert(root):
    if(root==None):
        return root
    
    node=TreeNode(root.val,root.right,root.left)
    
    
    node.left=invert(node.left)
    node.right=invert(node.right)
    
    return node


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return invert(root)