# Qus:https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

"""
Intiution : just find the total 
get the subtree sum 
get the other sum by sustracting the sum from total 
multiply both sum and keep track of max product of these two sum

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getTotalSum(root):
    if(root == None):
        return 0

    a = getTotalSum(root.left)
    b = getTotalSum(root.right)

    return root.val + a + b


def setMaxProduct(root, maxProduct, total):

    if(root == None):
        return 0

    a = setMaxProduct(root.left, maxProduct, total)

    maxProduct[0] = max(maxProduct[0], (total - a)*a)

    b = setMaxProduct(root.right, maxProduct, total)
    maxProduct[0] = max(maxProduct[0], (total - b)*b)

    return a + b + root.val


class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        totalSum = getTotalSum(root)
        print totalSum

        maxProduct = [0]
        setMaxProduct(root, maxProduct, totalSum)
        return maxProduct[0] % (10**9+7)
