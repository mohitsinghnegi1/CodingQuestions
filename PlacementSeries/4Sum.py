# Qus: https: // leetcode.com/problems/4sum/
# resource: https: // www.youtube.com/watch?v = 4ggF3tXIAp0 & list = PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma & index = 20


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        out = []

        # 1) find two number sum =sum1
        # 2) find target-sum1
        # 3) using binary search find set which is having target sum

        i = 0
        while(i < n-3):

            j = i+1

            while(j < n-2):

                # now we have first two element

                need = target-nums[i]-nums[j]

                l = j+1
                r = n-1

                while(l < r):

                    sum1 = nums[l]+nums[r]

                    if(sum1 < need):

                        l += 1
                        while(l < r and nums[l] == nums[l-1]):
                            l += 1

                    elif(sum1 > need):

                        r -= 1
                        while(l < r and nums[r] == nums[r+1]):
                            r -= 1

                    else:
                        # nums[l]+nums[r]==need then we need to push to out
                        quadruplets = [nums[i], nums[j], nums[l], nums[r]]
                        out.append(quadruplets)

                        # skip left dublicates
                        l += 1
                        while(l < r and nums[l] == nums[l-1]):
                            l += 1
                        # skip right dublicates
                        r -= 1
                        while(l < r and nums[r] == nums[r+1]):
                            r -= 1

                # skip dublicates
                j += 1
                while(j < n-2 and nums[j] == nums[j-1]):
                    j += 1

            # skip dublicates
            i += 1
            while(i < n-3 and nums[i] == nums[i-1]):
                i += 1

        return out
