# QUs:https://leetcode.com/problems/majority-element-ii/submissions/
# Boyer-Moore Voting Algorithm

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count1 = count2 = 0
        me1 = me2 = None

        for el in nums:
            if(el == me1):
                count1 += 1
            elif(el == me2):
                count2 += 1
            elif(count1 == 0):
                me1 = el
                count1 += 1
            elif(count2 == 0):
                me2 = el
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        o = []
        if(nums.count(me1) > len(nums)/3):
            o.append(me1)
        if(nums.count(me2) > len(nums)/3):
            o.append(me2)

        return o
