# QUs: https: // leetcode.com/problems/sort-colors/

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # dutch national flag algorithm
        l, m, r = 0, 0, len(nums)-1

        while(m <= r):

            # if nums[m]==0 swap with l increment left
            # elif nums[m]==2 swap with r decrement right
            # else increment m
            # Note dont use 3 if conditions else it will give wrong ans

            if(nums[m] == 0):
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1

            elif(nums[m] == 2):
                nums[r], nums[m] = nums[m], nums[r]
                r -= 1
            elif(nums[m] == 1):
                m += 1

        # print nums
