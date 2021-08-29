# QUs:https://leetcode.com/problems/patching-array/

# https://www.youtube.com/watch?v=N-tcCOCNSZY
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int

        increase reach max  by added elment time we add element to output list
        if element we need to add in output is already in list then patch count will
        not increase outher wise we will increase patch count - let say 9 is the second 
        number in list and out max patch is 7 then 8 will be added to out list
        """

        
        
        
        max_range = 0
        patch_count = 0
        i = 1
        j = 0
        
        while(max_range<n):
            
            if(j<len(nums)):
                
                # step 1
                if(i<nums[j]):
                    if(max_range<i):
                        patch_count += 1
                        max_range += i
                        
                    
                elif(i==nums[j]):
                    while(j<len(nums) and nums[j]==i ):
                        max_range += nums[j]
                        j+=1
                i += 1
                
            else:
                
                while(max_range<n):
                    patch_count+=1
                    max_range += (max_range + 1)
                
                
        return patch_count
            
            