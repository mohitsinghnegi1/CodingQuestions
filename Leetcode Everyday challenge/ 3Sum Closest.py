# Qus:https://leetcode.com/problems/3sum-closest/

# time complexity O(N*2)
import sys


class Solution(object):
    def threeSumClosest(self, nums, t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        curMindiff = sys.maxsize
        i = 0
        print nums
        minSum = sys.maxsize
        while(i < n):

            j = i + 1
            k = n - 1

            while(j < k):
                sum1 = nums[i]+nums[j]+nums[k]

                if abs(sum1 - t) < curMindiff:

                    curMindiff = abs(sum1 - t)
                    minSum = sum1
                    # print "=>",minSum

                    # print curMindiff,nums[i],nums[j],nums[k]
                if(curMindiff == 0):
                    return minSum
                if(sum1 > t):
                    k -= 1
                else:
                    j += 1

            i += 1
        return minSum
