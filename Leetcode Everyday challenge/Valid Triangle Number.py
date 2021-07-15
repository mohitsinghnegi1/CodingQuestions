# QUs:https://leetcode.com/problems/valid-triangle-number/

# Efficient solution  n**2 compleixity
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0

        """
        2 3 4 4
              i
        k   j       k+j>i ie 2+4>4
        Step2 : means if k + j > i that means all the any( k...j-1) + j > i
        
        reduce j 
        Step3: do step again until k<j
        
        Step4: reduce i do step 2 & 3 again until i becomes < 2
        

        """

        for i in range(2, len(nums)):
            j = 0
            k = i-1
            while(j < k):
                if(nums[j]+nums[k] > nums[i]):
                    count += k-j
                    k -= 1
                else:
                    j += 1
        return count


# TLE - O(N**3)
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if(nums[i]+nums[j] > nums[k]):
                        count += 1
        return count
