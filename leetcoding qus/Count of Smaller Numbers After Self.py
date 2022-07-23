# Qus:https://leetcode.com/problems/count-of-smaller-numbers-after-self/

# complexity : O(N**2)
# tag : sorting, binary search , merger sort [inversion count]

from bisect import bisect_left,bisect_right,insort

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """



        # given nums array you have to return a new array count where count[i] is the number of elemnt smaller to the right of nums[i]
        # O(n**2) solution



        smaller = []

        count = [0]*len(nums)



        for i in range(len(nums)-1,-1,-1):



            # now we need to find the number of smaller element to right
            # assume that smaller aray contains right element in the sorted fashion
            # we have to find smaller , How we can do that? we can use bisect_left to get element smaller then given element

            pos = bisect_left(smaller,nums[i])

            # here pos indicating number of element smaller then nums[i] to the right

            count[i] = pos

            # number we need to add current element in a sorted array
            insort(smaller,nums[i])

        return count

# Time complexity O(Nlogn) via inversion count

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        Things to rememeber

        every problem having condition i<j and a[i]>a[j] we can apply inversion count using merge sort

        always sort in decreasing order for ease
        remember to store the index as well O(N) extra space to count the inversion count wrt each element

        dont forget tho update the nums array & store intial i, j value for using it to update actual nums array


        """

        # we will use inversion count
        n = len(nums)
        count = [0]*n


        def merge(nums,i,mid,r):

            # print "for ",i,mid,r
            # assuming i,mid element are sorted in desc
            # assuming mid+1,j element are sorted in desc
            j = mid
            y = i
            k = []


            while(i<mid and j<=r):

                if(nums[i][0]>nums[j][0]):
                    # print "i , j ",i,j,nums
                    count[nums[i][1]]+= (r - j +1)
                    k.append(nums[i])
                    i+=1

                else:
                    k.append(nums[j])
                    j+=1


            k.extend(nums[i:mid])
            k.extend(nums[j:r+1])

            for x in range (y,r+1):
                nums[x] = k[x-y]

            # print "count is ",count
            # print nums[i:r+1]






        def mergesort(nums,l,r):
            # print l,r
            if(r - l >=1):

                mid = (l+r)/2

                mergesort(nums,l,mid)
                mergesort(nums,mid+1,r)

                merge(nums,l,mid+1,r)
                # print nums[l:r+1]


        nums2 = []


        for i in range(n):
            nums2.append((nums[i],i))


        mergesort(nums2,0,n-1)

        return count






