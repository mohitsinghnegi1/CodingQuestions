# Qus:https://leetcode.com/problems/most-frequent-subtree-sum/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d = defaultdict(int)
        maxFrequency = [0]

        def solve(root):

            if(root == None):
                return 0
            left = 0
            right = 0
            if(root.left):
                left = solve(root.left)
            if(root.right):
                right = solve(root.right)

            d[left+right+root.val] += 1
            # set max frequency
            maxFrequency[0] = max(maxFrequency[0], d[left+right+root.val])

            return left+right+root.val

        solve(root)

        ans = []

        for i in d:
            if(d[i] == maxFrequency[0]):
                ans.append(i)
        return ans
