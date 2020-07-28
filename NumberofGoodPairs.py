# QUs: https://leetcode.com/problems/number-of-good-pairs/
from collections import defaultdict
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=defaultdict(int)
        
        for i in nums:
            d[i]+=1
        ans=0
        for i in d:
            ans+=(d[i]*(d[i]-1))/2
        return ans