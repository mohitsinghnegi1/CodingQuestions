# Qus:https://leetcode.com/problems/unique-binary-search-trees-ii/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        d = {}
        # will return array of solution BST

        def generateBST(l, r):
            if((l, r) in d):
                return d[(l, r)]
            # in case l value > r return [None] means no left child
            if(l > r):
                return [None]

            out = []

            for i in range(l, r+1):
                # assuming that TreeNode(i) as a root value
                # what are the possible left BST
                leftBSTS = generateBST(l, i-1)
                # what are the possible right BST
                rightBSTS = generateBST(i+1, r)

                for left in leftBSTS:

                    for right in rightBSTS:
                        # we are trying all possible left and right to generate all possible BST
                        mid = TreeNode(i)
                        mid.left = left
                        mid.right = right
                        out.append(mid)
            # return Possible BST in range l .. r
            d[(l, r)] = out
            return d[(l, r)]

        # generateBST(1,n) will return all the valid BST have root value between 1 to n
        return generateBST(1, n)
