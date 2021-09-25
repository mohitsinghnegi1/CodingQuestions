# Qus:https://leetcode.com/problems/maximum-sum-circular-subarray/


import sys
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Intution 2 cases
        1. max subarray lies in middle of array (excluding the circlular creteria)
        2. some part lies at end and some part lies at beginig
        
        so to handle first case we need to do regular candanes algorithm
        
        but to handle second case we need to find min subarray sum and exclude the subarray from        total array and at the end take the max of both the possible case .
        Corner case : when all are negative the total as well as max subarray will comes out to be zero in that case we need to return max eleemnt from the array
        
        
        
        """
        
        
        
        max_so_far = 0
        max_so_far_positive = 0
        max1 = max2 = 0
        maxel = -sys.maxsize
        n = len(nums)
        total = 0
        for i in range(n):
            if(max2+nums[i]<0):
                max2 = 0
            else:
                max2 += nums[i]
                max_so_far_positive = max(max_so_far_positive,max2)
                
            maxel = max(maxel,nums[i])
            total += nums[i]
            nums[i] = -nums[i]
            if(max1+nums[i]<0):
                max1 = 0
            else:
                max1 += nums[i]
            # max1 = max(max1,nums[i]+max1,0)
            max_so_far = max(max1,max_so_far)
        # now we got min subarray sum
        # substract it to get max subarray sum
        # print total
        total += max_so_far # dont include min subarray sum
        # print max_so_far
        return max(total,max_so_far_positive) if max(total,max_so_far_positive)!=0 else maxel
        
                
                    
        
        
        
        
        
        
        
        
        
            
            
                
                
            