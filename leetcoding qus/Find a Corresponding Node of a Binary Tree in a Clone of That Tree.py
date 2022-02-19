# Qus:https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """

        # if all values are unique
#         ptr=cloned

#         stack=[]
#         stack.append(ptr)
#         if(ptr.val==target.val):
#             return ptr

#         while(stack):
#             node=stack.pop()
#             if(node.left):
#                 if(node.left.val==target.val):
#                     return node.left
#                 stack.append(node.left)
#             if(node.right):
#                 if(node.right.val==target.val):
#                     return node.right
#                 stack.append(node.right)

        # if dublicate values are allowed

        stack = []
        if(original == target):
            return cloned
        stack.append([original, cloned])

        while(stack):
            node1, node2 = stack.pop()

            if(node1.left):

                if(node1.left == target):
                    return node2.left

                stack.append([node1.left, node2.left])

            if(node1.right):

                if(node1.right == target):
                    return node2.right

                stack.append([node1.right, node2.right])
