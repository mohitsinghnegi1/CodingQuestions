# Qus:https://leetcode.com/problems/binary-tree-tilt/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        
        def __init__(self):
            self.tilt = 0
        """
        :type root: TreeNode
        :rtype: int
        """
        def absTilt(root):
            if(root==None):
                return 0
            
            leftSum = absTilt(root.left)
            rightSum = absTilt(root.right)
            
            sum1 = root.val + leftSum + rightSum
            
            root.val = abs(leftSum-rightSum)
            
            self.tilt+=root.val
            
            return sum1
        
        self.tilt = 0
        
        absTilt(root)
        
        return self.tilt
        
        