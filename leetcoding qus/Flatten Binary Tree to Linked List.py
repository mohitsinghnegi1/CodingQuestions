# Qus: https: // leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if(root == None or root.left == None and root.right == None):
            return

        stack = []

        # dont modify root
        ptr1 = root

        # the idea is to to append right child first then left child insidee the stack
        # so that left child we access first

        if(root.right):
            stack.append(root.right)
        if(root.left):
            stack.append(root.left)

        # after accessing left and right child node mark the left node as None
        ptr1.left = None
        ptr1.right = None

        while(stack):
            # access the node
            node = stack.pop()

            if(node.right):
                stack.append(node.right)
            if(node.left):
                stack.append(node.left)

            # mark the node left as none
            node.left = None
            node.right = None
            ptr1.right = node
            ptr1 = ptr1.right


# easy to understand iterative approach  also rember how we do preorder triversal using stack
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution3(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if(root == None):
            return root
        stack = []
        stack.append(root)
        while(stack):
            node = stack.pop()
            if(node.right):
                stack.append(node.right)
            if(node.left):
                stack.append(node.left)
            if(stack):
                # whatever will be processed next will be the right child of current poped node
                node.right = stack[-1]
                node.left = None
        return root
