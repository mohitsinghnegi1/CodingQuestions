# Qus:https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

#using recursion

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if(len(matrix)==0):
            return 0
        
        n=len(matrix)
        m=len(matrix[0])
        
        def bfs(i,j,length,prev=-sys.maxsize):
            
            #base case if it comes to boundary and already visited
            if(i<0 or i>=n or j<0 or j>= m or matrix[i][j]<=prev or matrix[i][j]=='#'):
                return length
            
            temp=matrix[i][j]
            
            #mark this node as # to indicate that this cell is already visited
            matrix[i][j]='#'
            
            left=bfs(i,j-1,length+1,temp) 
            right=bfs(i,j+1,length+1,temp)
            top=bfs(i-1,j,length+1,temp)
            bottom=bfs(i+1,j,length+1,temp)
            
            #undo the cell marked
            matrix[i][j]=temp
            
            #return the max length out of all directions
            return max(left,right,top,bottom)
        

        max_so_far=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_so_far=max(bfs(i,j,0),max_so_far)
        return max_so_far
    
    
    
    # efficient using memorization
    
    class Solution(object):
        def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if(len(matrix)==0):
            return 0
        
        n=len(matrix)
        m=len(matrix[0])
        
        global d
        d={}
        
        
        #no need to track length
        #we need to remember only ans for current cell 
        #becuse if we try to remember ans for child cell it will result wrong ans 
        #as child cell ans depending on prev
        
        def bfs(i,j,prev=-sys.maxsize):
            global d
            
            
            #base case if it comes to boundary and already visited
            if(i<0 or i>=n or j<0 or j>= m or matrix[i][j]<=prev or matrix[i][j]=='#'):
                return 0
            
            if(d.get((i,j))!=None):
                return d[(i,j)]
            
            temp=matrix[i][j]
            
            #mark this node as # to indicate that this cell is already visited
            matrix[i][j]='#'
            
            left=1+bfs(i,j-1,temp) 
            
            right=1+bfs(i,j+1,temp)
            
            top=1+bfs(i-1,j,temp)
            
            bottom=1+bfs(i+1,j,temp)
            
            
            #undo the cell marked
            matrix[i][j]=temp
            
            d[(i,j)] = max(left,right,top,bottom)
            #return the max length out of all directions
            return d[(i,j)]
        

        max_so_far=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_so_far=max(bfs(i,j),max_so_far)
        return max_so_far
    
    
    # most efficient - no need to mark visited as prev will dothe work
    
    class Solution(object):
        def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if(len(matrix)==0):
            return 0
        
        n=len(matrix)
        m=len(matrix[0])
        
        global d
        d={}
        
        
        #no need to track length
        #we need to remember only ans for current cell 
        #becuse if we try to remember ans for child cell it will result wrong ans 
        #as child cell ans depending on prev
        
        def bfs(i,j,prev=-sys.maxsize):
            global d
            
            
            #base case if it comes to boundary and already visited
            if(i<0 or i>=n or j<0 or j>= m or matrix[i][j]<=prev):
                return 0
            
            if(d.get((i,j))!=None):
                return d[(i,j)]
            
            temp=matrix[i][j]
            
            #mark this node as # to indicate that this cell is already visited
          
            
            left=1+bfs(i,j-1,temp) 
            
            right=1+bfs(i,j+1,temp)
            
            top=1+bfs(i-1,j,temp)
            
            bottom=1+bfs(i+1,j,temp)
                        
            d[(i,j)] = max(left,right,top,bottom)
            #return the max length out of all directions
            return d[(i,j)]
        

        max_so_far=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_so_far=max(bfs(i,j),max_so_far)
        return max_so_far