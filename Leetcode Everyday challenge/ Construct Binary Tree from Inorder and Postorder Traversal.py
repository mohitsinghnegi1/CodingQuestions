# Qus:https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# without optimizing space

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def solve(inorder,postorder):
            if(len(inorder)==0):
                return None
            

            mid = postorder.pop()
            root = TreeNode(mid)
            
            print mid
        
            
            index = inorder.index(mid)
            
            root.right = solve(inorder[index+1:],postorder)
            root.left = solve(inorder[:index],postorder)
            
            return root
            
        return solve(inorder,postorder)


# after optimizing spac
# O(n) time and O(n) space

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def solve(inorder,postorder,l,r):
            if(r-l==0):
                return None
            
            mid = postorder.pop()
            root = TreeNode(mid)
            
            # print mid
        
            
            index = inorder.index(mid)
            
            root.right = solve(inorder,postorder,index+1,r) # process right one -> after processing postorder will left with only nodes in the left of root
            root.left = solve(inorder,postorder,l,index) # process left node
            
            return root
            
            
            
        r = len(inorder)
        l =0
            
        return solve(inorder,postorder,l,r)