# QUs:https://leetcode.com/problems/count-good-nodes-in-binary-tree/
import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def solve(root, maxVal, ans):
    if(root == None):
        return
    if(root.val >= maxVal):
        ans[0] += 1
        maxVal = root.val

    solve(root.left, maxVal, ans)
    solve(root.right, maxVal, ans)

    return ans[0]


class Solution(object):

    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [0]
        return solve(root, -sys.maxsize, ans)
