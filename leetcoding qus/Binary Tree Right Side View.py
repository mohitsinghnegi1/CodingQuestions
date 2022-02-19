# Qus:https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import OrderedDict, deque


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if(root == None):
            return []

        d = OrderedDict()

        queue = deque([])
        queue.append((root, 0))

        while(queue):
            node, level = queue.popleft()
            d[level] = node.val
            if(node.left):
                queue.append((node.left, level+1))
            if(node.right):
                queue.append((node.right, level+1))

        return d.values()
