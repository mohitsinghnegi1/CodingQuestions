# QUs:https://leetcode.com/problems/delete-leaves-with-a-given-value/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        def delLeafNodeWith(parNode, target):
            # if cur node is empty return empty
            if(parNode == None):
                return None

            # set parent.left & parent.right value as a returned value from return value of a function
            parNode.left = delLeafNodeWith(parNode.left, target)
            parNode.right = delLeafNodeWith(parNode.right, target)
            if(parNode.val == target and parNode.left == None and parNode.right == None):
                return None
            else:
                # in case i am either not a leaf or i am a leaf node but not having value
                # equal to target
                return parNode

        # corner case [1,1,1] in this case we also need to set root as None
        root = delLeafNodeWith(root, target)
        return root
