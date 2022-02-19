# Qus:https://leetcode.com/problems/maximum-width-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # intution heap concept
        # use level:[left_min,right_max] to find the diameter of each level
        # remember formula 2n+1 2n+2 for 0 based
        if(root == None):
            return 0
        d = {}  # level:(lmax,rmax)
        # queue =[node,level,2*n+1||2n+2]
        queue = [(root, 0, 0)]
        while(queue):
            node, level, n = queue.pop(0)
            # update level info
            if(d.get(level)):
                l, r = d.get(level)
                d[level] = [min(n, l), max(n, r)]
            else:
                d[level] = [n, n]
            if(node.left):
                # number assigned to left node is 2*n+1
                queue.append((node.left, level+1, 2*n+1))
            if(node.right):
                # number assigned to left node is 2*n+2
                queue.append((node.right, level+1, 2*n+2))
        out = 0
        for l, r in d.values():
            # take the max range
            out = max(out, r-l+1)
        return out
