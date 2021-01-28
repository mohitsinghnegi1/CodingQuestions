# QUs:https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def recurse(node, level=0):
            # if current node is a leaf node
            # return current node itself, and the level of this leaf node
            if(node.left == None and node.right == None):
                # print [node,level]
                return [node, level]

            # if it is not the leaf node

            # we will use these to to keep track of left lca ancestor node for max level node
            # and right lca ancistor node for right max level node
            lan, llevel = None, 0  # left ancestor node
            ran, rlevel = None, 0  # right ancestor node

            # if there is a left child (basically we are doing postorder)
            if(node.left):
                # find lca in left of max level node
                lan, llevel = recurse(node.left, level+1)  # 7,3.    4,3
                # print "llevel",llevel
            if(node.right):
                # find lca in right ,(of max level leaf node)
                ran, rlevel = recurse(node.right, level+1)
                # print "rlevel",rlevel

            # backtrack
            # if we have both side node
            if(lan and ran):
                # check if both side max level are same ,if yes then this is the lca till now
                if(llevel == rlevel):
                    # we need to return then maxlevel always
                    return [node, llevel]
                # in case left or right have more more level leaf
                # then we use the same ansistor as before
                elif(llevel > rlevel):
                    return [lan, llevel]
                else:
                    return [ran, rlevel]

            # in case there is only one child then use the same node
            if(lan):
                return [lan, llevel]

            if(ran):
                return [ran, rlevel]

        return recurse(root)[0]

        node, level = recurse(root)
        print level
        return node
