# Qus:https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        """
            DFS TYPE : LPR
            Calculate total sum first that do LPR 
            or just do right parent left
        """
        # this sum1 will be used to assign sum value in right root left order
        global sum1
        sum1 = 0

        def rpl(root):
            global sum1
            if(root == None):
                return

            # as soon as we are at the rightest node we will update the sum1 value with root.val + sum1
            if(root.left == None and root.right == None):
                root.val = root.val + sum1
                sum1 = root.val
                return

            # move to the right first
            rpl(root.right)
            # assign root value as its own value + the updated sum1 value
            root.val = root.val + sum1
            # also update the sum ,so that left nodes also get the updated value
            sum1 = root.val
            rpl(root.left)

        rpl(root)
        return root
