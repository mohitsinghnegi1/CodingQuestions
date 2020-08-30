# QUs: https: // leetcode.com/problems/find-the-duplicate-number/


class Solution:
    def findDuplicate(self, nums):

        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            #print tortoise,hare
            if(tortoise == hare):
                break

        # start fast ie hare from zero location and move one step at a time
        # they will eventually meet at the element  which is dublicate
        print tortoise, hare
        hare = nums[0]
        while(hare != tortoise):
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare
