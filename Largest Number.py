# Qus:https://leetcode.com/problems/largest-number/

# time complexity O(n^2)
#bubble sort logic
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # using bubble sort logic
        nums=map(str,nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]>nums[j]+nums[i]):
                    nums[i],nums[j]=nums[j],nums[i]
        
        nums.reverse()
        return '0' if nums[0]=='0' else "".join(nums)

# time complexity O(nlog(n))
# cmp function in python

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # argument are reverse here x is 2nd elemnt and y is first element
        # if -1 means 
        def mycmp(x,y):
            # print x+y,y+x
            return -(int(x+y)-int(y+x))
            
        nums=map(str,nums)
        nums.sort(cmp=mycmp)
        return '0' if nums[0]=='0' else "".join(nums)
    
    