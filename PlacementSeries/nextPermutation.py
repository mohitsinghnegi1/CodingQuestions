# Qus:https://leetcode.com/problems/next-permutation/submissions/


import bisect


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if(len(nums) == 0):
            return

        max1 = nums[-1]
        i = len(nums)-2

        while(i >= 0):
            if(nums[i] < max1):
                pos1 = i

                j = pos1+1
                k = len(nums)-1

                #sort the numbers on the right of pos1

                while(j < k):
                    nums[j], nums[k] = nums[k], nums[j]
                    j += 1
                    k -= 1

                #here i am searching for nums[pos1]+1 bec we need a number which is just greater                   #then element at positon  pos1
                #bisect_left will give pos of just greater number
                #i havn't used bisect right bec if number you are searching is same as
                #greatest number in the right side then it will give pos which is not in range
                #of the array and will give out of bound exception

                pos2 = bisect.bisect_left(
                    nums, nums[pos1]+1, pos1+1, len(nums))

                #print nums[pos1],pos2,nums
                #swap pos1 with number which is on the right side and just greater then cur number
                nums[pos1], nums[pos2] = nums[pos2], nums[pos1]

                break

            #update max
            max1 = nums[i]
            i -= 1

        else:
            #if full array is in decending order the make it in accesnding order
            nums.sort()
