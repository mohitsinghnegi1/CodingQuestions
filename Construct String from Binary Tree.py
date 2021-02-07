# Qus:https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        global s
        s = ""

        def preorder(root):
            global s

            if(root == None):
                return
            s += str(root.val)

            if(root.left == None and root.right == None):
                return

            s += '('
            preorder(root.left)
            s += ')'
            if(root.right):
                s += '('
                preorder(root.right)
                s += ')'

        preorder(t)
        return s
