# Qus:https://leetcode.com/problems/longest-univalue-path/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def longestpath(root):
    left,left_max=0
    right,right_max=0
    if(root.left):
        if(root.left.val==root.val):
            left=longestpath(root.left)
    if(root.right):
        if(root.right.val==root.val):
            right=longestpath(root.right)
    cur_max=root.val+left+right
    return max(cur_max,left_max,right_max)


class Solution(object):
    
    def __init__(self):
        self.longestPath=0
        
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        if(root==None):
            return 0
        def longestpath(root):
            if(not root.left and not root.right):
                self.longestPath=max(self.longestPath,1)
                return 1
            # update possible max if possible
            left=right=0
            if(root.left):
                l=longestpath(root.left)
                if(root.val==root.left.val):
                    left=l
            if(root.right):
                r=longestpath(root.right)
                if(root.val==root.right.val):
                    right=r
            
            self.longestPath=max(self.longestPath,1+left+right)
    
            return 1+max(left,right)
        longestpath(root)
        
        return self.longestPath-1