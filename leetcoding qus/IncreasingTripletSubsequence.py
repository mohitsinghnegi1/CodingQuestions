# Qus:https://leetcode.com/problems/increasing-triplet-subsequence/


#optimized brute force
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #brute force TLE - > litle optimization increase the efficience
        #if(nums[i]<nums[j]-1) this condition 
        for i in range(len(nums)-2):
            for j in range(i+2,len(nums)):
                if(nums[i]<nums[j]-1):
                    for k in range(i+1,j):
                        if(nums[i]<nums[k]<nums[j]):
                            return True
        return False
                    
            
            
#sol 2 -- nice algorithm can be used for n 

import sys
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x=y=sys.maxsize
        
        for i in nums:
            if(i<=x):
                x=i
            elif(i<=y):
                y=i
            else:
                return True
        return False
                    
            