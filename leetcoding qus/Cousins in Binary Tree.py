# QUs:https://leetcode.com/problems/cousins-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if(x == y):
            return False

        d = {}

        def dfs(root, par, level=0):

            if(root == None):
                return
            # set the info of node parent and level of each node in a tree
            d[root.val] = (level, par)

            dfs(root.left, root, level+1)
            dfs(root.right, root, level+1)

        par = None
        dfs(root, par)

        # if par are same return fasle or level are not equal
        if(d[x][1] == d[y][1] or d[x][0] != d[y][0]):
            return False

        return True
