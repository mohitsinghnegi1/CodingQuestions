# Qus:https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getBalancedBST(nums):

    if(len(nums) == 0):
        return None

    if(len(nums) == 1):
        return TreeNode(nums[0])

    mid = len(nums)/2
    root = TreeNode(nums[mid])
    root.left = getBalancedBST(nums[:mid])
    root.right = getBalancedBST(nums[mid+1:])
    return root


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return getBalancedBST(nums)
