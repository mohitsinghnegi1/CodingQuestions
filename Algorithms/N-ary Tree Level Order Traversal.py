# Qus:https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if(root == None):
            return root

        out = []

        queue = deque()
        queue.append(root)

        while(queue):
            level = deque()
            ans = []
            while(queue):
                node = queue.popleft()
                for child in node.children:
                    level.append(child)

                ans.append(node.val)

            out.append(ans)
            queue = level
        return out
