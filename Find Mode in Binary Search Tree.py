# Qus:https://leetcode.com/problems/find-mode-in-binary-search-tree/


# using O(n) and O(n) space


from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution2(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        d = defaultdict(int)
        max1 = [0]

        def inorder(root):
            if(root == None):
                return
            inorder(root.left)
            d[root.val] += 1
            max1[0] = max(d[root.val], max1[0])
            inorder(root.right)

        inorder(root)

        out = []
        for i in d:
            if(d[i] == max1[0]):
                out.append(i)
        return out


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
            Intution : 2 pass
            Keep global varibale to keep track of prev visited node in inorder treversal 
            Also keep track of max , and maxF till now
            In first pass you will get the max Frequency
            In next inorder pass fine the frequency and update the element in out arr when you
            encounter the same frequency
        
            Time complexity O(n) space complexity O(1)
        """

        if(root == None):
            return []

        prev = [None]
        maxF = [1]
        max1 = [1]

        def inorder(root):

            if(root == None):

                return
            inorder(root.left)

            if(prev[0] != None and prev[0] == root.val):
                max1[0] += 1
                maxF[0] = max(maxF[0], max1[0])
            else:
                max1[0] = 1
                prev[0] = root.val

            inorder(root.right)

        inorder(root)

        print maxF[0]

        out = []
        prev = [None]

        def inorder2(root):

            if(root == None):

                return
            inorder(root.left)

            if(prev[0] != None and prev[0] == root.val):
                max1[0] += 1
                if(max1[0] == maxF[0]):
                    out.append(root.val)
            else:
                max1[0] = 1
                if(max1[0] == maxF[0]):
                    out.append(root.val)
                prev[0] = root.val

            inorder(root.right)

        inorder2(root)

        return out
