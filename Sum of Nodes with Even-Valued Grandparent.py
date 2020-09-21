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

        global sum1
        sum1 = 0

        def findSum(root):
            global sum1

            if(root == None):
                return

            if(root.val % 2 == 0):
                # if the value of root is even then add sum of its grandchilderens
                if(root.left):

                    if(root.left.left):
                        sum1 += root.left.left.val
                    if(root.left.right):
                        sum1 += root.left.right.val

                if(root.right):

                    if(root.right.left):
                        sum1 += root.right.left.val
                    if(root.right.right):
                        sum1 += root.right.right.val
            # move in its childs
            if(root.left):
                findSum(root.left)
            if(root.right):
                findSum(root.right)

        findSum(root)

        return sum1
