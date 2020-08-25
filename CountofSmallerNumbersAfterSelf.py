# Qus:https://leetcode.com/problems/count-of-smaller-numbers-after-self/


import bisect

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smaller=[]
        print bisect.bisect_left(smaller,3)
        
        out=[0]*len(nums)
        
        #move from right to left 
        #insert each visted elemnt into smaller array in sorted manner using 
        #binary search so that we can get the number of smaller elemnt by
        #using smaller array and binary search in O(logn) time complexity
        
        for i in range(len(nums)-1,-1,-1):
            
            
            out[i]=bisect.bisect_left(smaller,nums[i])
            
            bisect.insort(smaller,nums[i])
        return out
            
            
            
            
            