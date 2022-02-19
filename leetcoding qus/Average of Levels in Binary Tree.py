# Qus:https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        queue = [root]
        
        ans = []
        
        while(queue):
            
            total = 0
            count = len(queue)
            
            nextlevelNodes = []
            
            while(queue):
                
                node = queue.pop()
                
                total += node.val
                
                if(node.left):
                    nextlevelNodes.append(node.left)
                if(node.right):
                    nextlevelNodes.append(node.right)
                    
            ans.append((total+0.0)/count)
            
            queue = nextlevelNodes
            
        return ans
        
                
        
        
        