# Qus:https://leetcode.com/problems/path-sum-iii/


class Solution(object):
    def __init__(self):
        self.ans = 0
    
    def dfs(self,root,target):
        # print target
        if(root==None):
            return 
        
        
        self.considerItRootNode(root,target)
        
        self.dfs(root.left,target)
        self.dfs(root.right,target)
    
    def considerItRootNode(self,root,target):
        # print target
        if(root==None):
            return 
        target -= root.val
        if(target==0):
            self.ans+=1
        
        
        self.considerItRootNode(root.left,target)
        self.considerItRootNode(root.right,target)
    

    
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        """
            Intution:
            traverse in each node , consider it first node of the path which get our target sum
        
        """
        
        
        
        self.ans = 0
        
        if(root==None ):
            return 0
        
        self.dfs(root,sum) # this will give me the number of possible ways to get the target sum
        
        return self.ans