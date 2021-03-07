# Qus:https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

from collections import defaultdict
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# -- brute force approch and more space


def constructTree(root, p, q, d):
    if(root == None):
        return
    d[root.left] = root
    d[root.right] = root
    constructTree(root.left, p, q, d)
    constructTree(root.right, p, q, d)


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # construct child-> [parents]
        d = defaultdict(TreeNode)
        constructTree(root, p, q, d)

        # triverse from child to parent to get lowest common Ansestor

        d[root] = None
        ptr = p

        ansistors = {}

        # we can use dict
        # we need to get all the ansisters of this node p
        while(ptr):
            ansistors[ptr] = True
            ptr = d[ptr]

        # we need to get ansistors of node q ans as soon as
        # the ansistore of q available on ansistors dict we need to return it
        ptr = q

        while(ptr):
            if(ansistors.get(ptr) != None):
                return ptr
            ptr = d[ptr]


# better approach without using O(1)space
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution2(object):
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def ansistor(root):
            if(root == None):
                return False

            left = ansistor(root.left)
            mid = root == p or root == q
            right = ansistor(root.right)

            if(mid+left+right >= 2):
                self.ans = root

            return left or mid or right

        ansistor(root)
        return self.ans

        # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution3(object):
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def solve(root):

            if(root == None):
                return False

            l = solve(root.left)
            m = root == p or root == q
            r = solve(root.right)

            if(l + m + r >= 2):
                self.ans = root

            return l or r or m

        solve(root)
        return self.ans
