# Qus:https://leetcode.com/problems/longest-increasing-subsequence/

# O(n*2) using dp
from bisect import bisect_left


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1]*n
        # dp[0]=1

        for i in range(1, n):

            for j in range(i):

                if(nums[j] < nums[i]):
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)


# using sub array and binary search


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # longest increasing subsequence in O(nlogn)
        # draw graph for intution
        # order is not maintained in this ans only the length

        sub = []
        for val in nums:
            idx = bisect_left(sub, val)  # gives insertion point
            if(idx == len(sub)):
                sub.append(val)
            else:
                sub[idx] = val

        return len(sub)
