# Qus:https://leetcode.com/problems/first-missing-positive/

import sys
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Intution: 
            
            number <= 0 and number > len(nums) can't be a soltuion . why? 
            Hint : we need to find the first smallest <POSITIVE> number 
            
            
            Algo:
                1. change all the -ve value and value > n to infinity (In order to avoid them from our solution space)
                
                2. Traverse in the array , if abs(value) is not infinity , we need to mark this element as present , so
                for that we will change the element present at index i - i with - abs(value[i-1]) {This will indicate that i+1 value is present}
                
                
                3. TO find the first missing positive number , we need to traverse in the array and find the first positive value . and our ans would be i+1 
                
                # Special case : what if there is no missing element in the array 
                # in this case the ans would be n+1
        
        
        
        """
        
        
        
        
        n = len(nums)
        
        # change the sign of negative number to +ve also we need to change the number to infinity  so that we dont consider this number as a solution
        # also change the number which is greater then n to infi 
        
        for i in range(n):
            if(nums[i]<=0 or nums[i]>n):
                nums[i] = sys.maxsize
        
        # once this is done 
        # we need to change the sign of number exist at pos num[i] with its -ve value
        
        # while treversing we need to consider the absolute value 
        
        
        for i in range(n):
            absNum = abs(nums[i])
            if(absNum !=sys.maxsize):
                
                
                # we need to change the sign of number exist at index absNum -1 
                # which mean that the number absNum exist
                
                nums[absNum-1] = -abs(nums[absNum-1])
        
        
        # traverse in the arrray and find the index which is non -ve 
        # ans will be index + 1
        
        for i in range(n):
            if(nums[i]>0):
                return i+1
        
        
        # Special case : what if there is no missing element in the array 
        # in this case the ans would be n+1
        
        
        return n+1
        
        
                
                
                
                
            