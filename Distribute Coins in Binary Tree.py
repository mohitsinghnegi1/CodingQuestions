# QUs:https://leetcode.com/problems/distribute-coins-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.totalMoves = 0

    def util(self, root):
        if(root == None):
            return 0

        leftMoves = rightMoves = 0

        if(root.left):
            leftMoves = self.util(root.left)
            # print "lm",leftMoves
        if(root.right):
            rightMoves = self.util(root.right)
            # print "rm",rightMoves

        # let suppose i am a leaf node with no left and right child
        self.totalMoves += (abs(leftMoves) + abs(rightMoves))

        return leftMoves + rightMoves + root.val - 1

    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.util(root)
        return self.totalMoves
