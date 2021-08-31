# Qus:https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(nums[0]<=nums[-1]):
            return nums[0]
        
        
        l,r=0,len(nums)
        
        while(l<r):
            mid = (l + r)/2
            
            if(nums[mid]>=nums[l]):
                l += 1
            else:
                r = mid # since mid could be the ans so we are taking 1 more
        return nums[l]