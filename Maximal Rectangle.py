# Qus:https://leetcode.com/problems/maximal-rectangle/

# time complexity is O(n*2n)
# 2*n for calculating max Rectangle for a row
# n for number of rows in the matrix
def largestRectangleArea(h):
        """
        :type heights: List[int]
        :rtype: int
        """
        # try to draw a graph first
        # remember it is similar to brute force approack
        # formulat to calculate area is (i-stack[-1]-1)*h[pop] after poping out the               # element
        # in case of empty stack , means it is the smallest element till now so 
        # formula for it is (i)*h[pop]
        stack=[]
        i=0
        max1=0
        
        while(i<len(h)):
            if(stack==[] or h[stack[-1]]<=h[i]):
                stack.append(i)
                i+=1
            else:
                li=stack.pop()
                if(stack==[]):
                    max1=max(max1,(i)*h[li])
                else:
                    
                    max1=max(max1,(i-stack[-1]-1)*h[li])
                    
        
        while(stack):
            li=stack.pop()
            if(stack==[]):
                max1=max(max1,(i)*h[li])
            else:
                max1=max(max1,(i-stack[-1]-1)*h[li])
        
        return max1




class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if(len(matrix)==0 or len(matrix[0])==0):
            return 0
        
        max1=0
        h=[0 for i in range(len(matrix[0]))]
        
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # make sure the matrix elemnts is string 
                
                if(matrix[i][j]=='1'):
                    
                    h[j]+=1
                else:
                    h[j]=0
            # we have a calculated height arr for row i
            # now can can pass to largestRectangleArea to calculate what is the 
            # largest rectangle possible
            # same histrogram approach to calculate matrix rectangle area
            max1=max(max1,largestRectangleArea(h))
            
        return max1
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        