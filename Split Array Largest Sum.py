# Qus:https://leetcode.com/problems/split-array-largest-sum/
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        """
        brute force could be use a linear traversal form max(arr)--> min val that we can select in         
        for a single bucket (this will increase number of bucket but reduce the average) to                 
        sum(arr) --> max possible (this will reduce the number of bucket but increase the average)
        ** so we need to balance it out such that the averge is as min as possible under the bucket
        
        inner for loop will count the number of buckets and outer for loop will check from max(arr)
        to sum(arr) which min average satisfies the condition of max bucket being m
        # time complexity is O(n**2)
        
        Optimized versionL: use binary search to find the maxPossible averge (instead of using for         
        loop for that)  time complexity is O(nlogn)
        
        
        """

        # case where len of array < m
        if len(nums) < m or m <= 0:
            return -1

        l = max(nums)
        r = sum(nums)+1  # to avoid corner cases

        while(l < r):

            mid = l+(r-l)/2  # mid is the largest sum allowed

            part = 1
            curSum = 0

            for val in nums:
                if curSum+val > mid:
                    part += 1
                    curSum = val
                else:
                    curSum += val

            if part > m:
                # part need to be decreased , so we need to increase the allowed sum
                l = mid+1
            else:
                # we have sufficient number of parts , lets utize them if possible to
                # decrease the average
                r = mid

        return l
