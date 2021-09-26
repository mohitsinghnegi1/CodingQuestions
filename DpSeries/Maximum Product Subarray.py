# QUs: https://leetcode.com/problems/maximum-product-subarray/

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 2 3 -2 4
        
        # max => 2 max(3,2*3,2*3) = 6 max(-2,6*-2,6*-2) = -2 max(4,-2*4,-12*4) = 4
        
        # min => 2 max(3,2*3,2*3) = 6 min(-2,6*-2,6*-2) = -12 min() = -48
        
        
        max_so_far = nums[0]
        n = len(nums)
        prevMax = nums[0]
        prevMin = nums[0]
        
        for i in range(1,n):
            curMax = max(nums[i],nums[i]*prevMax,nums[i]*prevMin)
            curMin = min(nums[i],nums[i]*prevMax,nums[i]*prevMin)
            max_so_far = max(curMax,curMin,max_so_far)
            prevMax = curMax
            prevMin = curMin
            
        return max_so_far
            