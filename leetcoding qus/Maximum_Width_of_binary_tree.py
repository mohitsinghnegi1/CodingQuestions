# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #sol 1
        
        
#         if(root==None):
#             return 0
#         global width
#         width=1
#         global levels
#         levels=[]#this arry will maintain [l,r] min left and max right in the current level
#         for i in range(10000):
#             levels.append([sys.maxsize,0])
            
#         def calc_width(level,left,right):
#             global width
#             global levels
#             #print level
#             #i am checking what is the left most and rightmost  elemnt in each level and the calculating the width
#             if(left>sys.maxsize and levels[level][0]==sys.maxsize ):
#                 levels[level][0]=left
                
                
#             l=min(levels[level][0],left)
#             if(left<levels[level][0]):
#                 levels[level][0]=left
#             if(right>levels[level][1]):
#                 levels[level][1]=right

#             # print levels
#             width=max(width,levels[level][1]-levels[level][0]+1)
        
        
        
#         def bfs(root):
            
    
#             stack=[]
#             #second argument is pos
#             stack.append((root,1,1))
#             while(stack!=[]):
#                 node,level,pos=stack.pop()
                
#                 #put your logic here
#                 if(node.left and node.right):
#                     # print pos*2, pos*2+1,level
#                     calc_width(level+1,pos*2,pos*2+1)
#                 elif(node.left ):
#                     # print "left pos ",pos*2 ,level
#                     calc_width(level+1,pos*2,pos*2)
#                 elif(node.right):
#                     # print "right pos ",pos*2+1 ,level
#                     calc_width(level+1,pos*2+1,pos*2+1)
#                 #insert both child node inside stack 
#                 if(node.left):
#                     stack.append((node.left,level+1,pos*2))
#                 if(node.right):
#                     stack.append((node.right,level+1,pos*2+1))
#                 # print stack
#         #complexity O(n)
#         bfs(root)
        
      
#         return width
    
    
    
    
        #new solution 
        
        # use bfs
        #use for loop for each element in the queue (same level)
        #make sure you exaust one level node before calculating new level width
        
        if(not root):
            return 0
        
        queue=[]
        queue.append((root,0))
        max_len=0
        
        while(queue):
            max_len=max(max_len,queue[-1][1]-queue[0][1]+1)
            k=len(queue)
            for i in range(k):
                node,index=queue[0]
                print node.val,index
                if(node.left):
                    queue.append((node.left,2*index+1))
                if(node.right):
                    queue.append((node.right,2*index+2))
                queue.pop(0)
        return max_len
            
            
            
            
            
            
            
        
        
        