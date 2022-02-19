# QUs:https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def getTree(root):

            if(root == None):
                return 0
            if(root.left == None and root.right == None):
                return root.val

            left = getTree(root.left)
            right = getTree(root.right)

            if(left == 0):
                root.left = None
            if(right == 0):
                root.right = None

            return root.val+left+right

        return root if getTree(root) else None
