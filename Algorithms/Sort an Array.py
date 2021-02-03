# QUs:https://leetcode.com/problems/sort-an-array/
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge(nums, l, m, r):

            k = []

            b = l
            e = m+1
            while(b <= m and e <= r):

                if(nums[b] <= nums[e]):
                    k.append(nums[b])
                    b += 1
                else:
                    k.append(nums[e])
                    e += 1
                # print k

            while(e <= r):
                k.append(nums[e])
                e += 1
            while(b <= m):
                k.append(nums[b])
                b += 1

            # update original array
            x = 0
            for i in range(l, r+1):

                nums[i] = k[x]
                x += 1
            # print "galat",k,l,r
            # print nums

        def mergeSort(nums, l, r):

            if(r-l < 1):
                return nums

            mid = l+(r-l)/2
            # print l,mid,r
            mergeSort(nums, l, mid)
            mergeSort(nums, mid+1, r)
            merge(nums, l, mid, r)
            return nums

        return mergeSort(nums, 0, len(nums)-1)
