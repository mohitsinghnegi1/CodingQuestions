# Qus:https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init(self):
        self.ans = None
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        
        def getPoint(preorder,rootVal):
            
            breakpoint = -1
            
            j = len(preorder)-1
            while(j>0 and preorder[j]>rootVal ):
                breakpoint = j
                j-=1
            
            return breakpoint
            
            
        
        def construct(preorder):
            
            if(len(preorder)==0):
                
                return None
            
            root = TreeNode(preorder[0])
            
            if(len(preorder)==1):
                return root
            
            breakpoint = getPoint(preorder,root.val)
            # print breakpoint
            if(breakpoint==-1):
                # means all nodes lies in left side
                root.right = None
                root.left = construct(preorder[1:])
            else:
                root.right = construct(preorder[breakpoint:])
                
                root.left = construct(preorder[1:breakpoint])
                
            
            return root
        
    
        return construct(preorder)


# optimised version using binary search

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init(self):
        self.ans = None
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        
        def getPoint(preorder,rootVal):
            
            
            if(preorder[-1]<rootVal):
                return -1
        
            
            l=1
            r = len(preorder)
            
            while(l<r):
                
                mid = (l+r)/2
                
                if(preorder[mid]<rootVal and preorder[mid+1]>rootVal):
                    return mid+1
                
                if(preorder[mid]<rootVal):
                    l = mid+1
                else:
                    r = mid
            
            
            
            
            return l
            
            
        
        def construct(preorder):
            
            if(len(preorder)==0):
                
                return None
            
            root = TreeNode(preorder[0])
            
            if(len(preorder)==1):
                return root
            
            breakpoint = getPoint(preorder,root.val)
            # print breakpoint
            if(breakpoint==-1):
                # means all nodes lies in left side
                root.right = None
                root.left = construct(preorder[1:])
            else:
                root.right = construct(preorder[breakpoint:])
                
                root.left = construct(preorder[1:breakpoint])
                
            
            return root
        
    
        return construct(preorder)
            
            
# O(n ) solution


import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.idx = 0
        
        
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        
        
        def construct(preorder,parVal = sys.maxsize):
            
            # if there is no node
            if(self.idx>=len(preorder) or preorder[self.idx]>parVal):# case where current node at idx is > par val see example below
                return None
            
            root = TreeNode(preorder[self.idx])
            self.idx+=1
          
            
            # if there are more then one node 
            # case 1 , root contains only left nodes
            # case 2 root contains only right nodes
            # case 3 root contains left and right nodes
            
            root.left = construct(preorder,root.val) # treverse till parent node is > then child node
            # for example [5 3 1] 4
            # [5 2 1] 3
            
            # once we found a node whose parent is < the node value then we need to backtrack
            # here we are passing parent node bec , we always need to shift to right when parent node of current node is greater then the idx value and then repeat the same dec order process
            root.right = construct(preorder,parVal)
            
            return root
        
        self.idx = 0
        return construct(preorder)
    
    
            
            
            
            
            
            
            
            
            
            
            
            
            