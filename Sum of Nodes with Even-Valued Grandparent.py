# QUs:https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getSum(root):

            if(root == None):
                return 0

            sum1 = 0

            if(root.val % 2 == 0):

                if(root.left and root.left.left):
                    sum1 += root.left.left.val
                if(root.left and root.left.right):
                    sum1 += root.left.right.val

                if(root.right and root.right.left):
                    sum1 += root.right.left.val

                if(root.right and root.right.right):
                    sum1 += root.right.right.val

            return sum1 + getSum(root.left)+getSum(root.right)

        return getSum(root)
