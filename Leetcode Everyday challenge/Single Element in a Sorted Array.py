# Qus:https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = 0
        r = n - 1
        
        if(n==1):
            return nums[0]
        
        while(l<=r):
            
            mid = (l + r)/2
            
            if(mid%2==1):
                
                if(nums[mid-1]!=nums[mid]):
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                
                if(mid+1>=n):
                    return nums[mid]
                
                if(nums[mid]!=nums[mid+1]):
                    r = mid - 1
                else:
                    l = mid + 2
        return nums[l]
                    
                
            
            
        