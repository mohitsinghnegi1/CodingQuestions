import sys
# https://leetcode.com/problems/132-pattern/
# time complexity O(2*n)
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """
        Intution:

        keep track of second max, maintain the highest element within stack

        Once you reach a condition where cur elemtn is less then second max then return true

        Approach : Monotonic decreasing Stack

        ...[AiMin]... [AjMax]... [AkSecondMax]...


        # Note : It is require to append new eleemnt into stack if stack[-1] < cur elemnt consider following case
        [1,3,2,4,5,6,7,8,9,10]  here 2 is the second max , 3 is the max , and 1 is the min


        """
        stack = []


        second_max = -sys.maxsize


        for i in range(len(nums)-1,-1,-1):

            if(stack and nums[i]<second_max):
                return True

            while(stack and stack[-1]<nums[i]):
                num = stack.pop()
                second_max = max(num,second_max)

            stack.append(nums[i])

        return False

