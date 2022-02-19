# QUs:https://leetcode.com/problems/subtree-of-another-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        """
            Time complexity O(n**2)
            
            Intution :
                for every same node(equal value) - consider this as root node and check all                      descendants) 
        
        """
        def isSubtree(s, t):
            if(s == None and t == None):
                return True
            if(s == None or t == None):
                return False

            if(s.val == t.val):
                return isSubtree(s.left, t.left) and isSubtree(s.right, t.right)
            else:
                return False

        def util(s, t):

            if(s == None):
                return False

            if(s.val != t.val):
                # we know if val are not equal we need to check other ways using or
                return util(s.left, t) or util(s.right, t)
            else:
                # if they are equal we should consider the node as a root node  and check
                # if they are same also we need to check other ways also
                return isSubtree(s, t) or util(s.left, t) or util(s.right, t)

        return util(s, t)
