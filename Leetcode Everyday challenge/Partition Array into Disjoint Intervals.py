# Qus:https://leetcode.com/problems/partition-array-into-disjoint-intervals/
# TIME COMPLEXITY O(N)
# SPACE COMPEXITY O(N)

class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        [5,0,3,8,6]
        
        
        maxLeft = 5 5 5 8 8
        minRight = 0 0 3 6 6
        
        
        
        """

        n = len(nums)
        maxLeft = [0]*n
        minRight = [0]*n

        max1 = 0
        for i in range(n):
            max1 = max(max1, nums[i])
            maxLeft[i] = max1

        min1 = nums[-1]

        for i in range(n-1, -1, -1):
            min1 = min(min1, nums[i])
            minRight[i] = min1

        for i in range(1, n):
            if(maxLeft[i-1] <= minRight[i]):
                return i
