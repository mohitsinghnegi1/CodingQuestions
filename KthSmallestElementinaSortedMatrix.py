# Qus:https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        #   solution using heap
        
        heap=[]
        
        #   create a heap and store all the elemnt from the first row
        for i in range(len(matrix[0])):
            
            #   push tuple (element,row,col) - heap will heapyfy based on this smallest elemnt
            #   row and col we are pushing to get element present in next row in same column               #   elemnt 
            heapq.heappush(heap,(matrix[0][i],0,i))
            
        #this variable keep track of number of smallest element poper out of stack    
        i=0
        
        #   now we need to pop out the min elemnt
        #   every time we pop smallest number from the heap 
        #   we will append the element in next row but in same col 
        #   (if inside boundry of matrix)
        #   this logic works bec we know that all element of row we seen that are greater
        #   then the poped elment so next smaller elemnt possibly will be the element in next           #   row,same column
        
        min1=None
        
        while(i<k):
            min1,row,col=heapq.heappop(heap)
            
            #if smallest elemnt is in last row then dont go to next row 
            if(row+1<len(matrix)):
                heapq.heappush(heap,(matrix[row+1][col],row+1,col))
            i+=1
        
        return min1
            