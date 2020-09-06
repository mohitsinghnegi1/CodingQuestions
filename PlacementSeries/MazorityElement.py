# Qus:https://leetcode.com/problems/majority-element/


# Resource :https://www.youtube.com/watch?v=AoX3BPWNnoE&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=15

from collections import defaultdict


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer-Moore Voting Algorithm

        # since count of mazority elemnt is greater then minority element
        # so mazority element will always cancel out the minority element

        if(len(nums) == 0):
            return None

        mel = nums[0]
        count = 0

        for el in nums:
            if(count == 0):
                mel = el

            if(mel == el):
                count += 1
            else:
                count -= 1

        return mel
