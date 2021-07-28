# Qus:https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isBalanced(self, root):
    if(root == None):
        return 0

    left = isBalanced(self, root.left)
    right = isBalanced(self, root.right)

    if(abs(left-right) > 1):
        self.ans = False

    return 1 + max(left, right)


class Solution(object):
    def __init__(self):
        self.ans = True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        isBalanced(self, root)

        return self.ans
