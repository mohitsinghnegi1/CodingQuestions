# QUs:https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
            Intution : use tree dp : pass min and max value till now
            calculate max difference as maxAbsdiff of cur node with all its ansister (range)
            update the range value using cur node val
            find maxAbsdiff in left and right subtree 
        """

        def getMax(root, sm, lg):

            if(root == None):
                return 0

            maxAbsdiff = max(abs(root.val-sm), abs(lg-root.val))

            sm = sm if sm < root.val else root.val
            lg = lg if lg > root.val else root.val

            leftMaxAbsdiff = getMax(root.left, sm, lg)
            rightMaxAbsdiff = getMax(root.right, sm, lg)

            # return max out of curnode maxAbsdiff , left subtree max abs diff and right subtree abs diff
            return max(maxAbsdiff, leftMaxAbsdiff, rightMaxAbsdiff)

        return getMax(root, root.val, root.val)
