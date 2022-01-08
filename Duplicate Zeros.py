class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        a = [0]*len(arr)
        
        zeroes = 0
        
        for i in range(len(arr)):
            
            if(arr[i]!=0):
                
                if(i+zeroes>=len(arr)):
                    break
                
                a[i+zeroes] = arr[i]
            else:
                zeroes+=1
        
        
        for i in range(len(arr)):
            arr[i] = a[i]
        
            
                
                
        # print a
        return a