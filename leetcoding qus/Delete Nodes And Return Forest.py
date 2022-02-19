# QUs:https://leetcode.com/problems/delete-nodes-and-return-forest/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        out = []
        to_delete = set(to_delete)

        def dfs(root, parent_exist):
            if(root == None):
                return None
            # if this node we want to delete
            # we will not add this node to out and move to next nodes with
            # parent_exist as false

            if(root.val in to_delete):
                dfs(root.left, False)
                dfs(root.right, False)
                # dereference root.left and root.right if
                root.left, root.right = None, None
                return None

            # if the node val does not exist in the delete array
            # either it is the root node
            # or this is the node after the node we have to delete
            if(not parent_exist):
                out.append(root)

            # we are setting left and right pointer (In case left and right node we need
            # to delete then we will automatically set to None)
            root.left = dfs(root.left, True)
            root.right = dfs(root.right, True)

            # we are directly returning root bec
            # in case of node that we want to delte we are alreadyh setting its left right             # as none
            return root

        dfs(root, parent_exist=False)
        return out
