# QUs:https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.memo = {}
        print root

    def recoverTree(self, root, val=0):

        if(root == None):
            return
        root.val = val
        self.memo[val] = True
        # move to left child
        self.recoverTree(root.left, val=2*val+1)

        # move to right child
        self.recoverTree(root.right, val=2*val+2)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        if(self.root == None):
            return False
        if(self.root.val == -1):
            # do recovery
            self.recoverTree(self.root)

        return self.memo.get(target, False)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
