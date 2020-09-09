# QUs: https: // leetcode.com/problems/reverse-pairs/


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i+1, n):
                if(nums[i] > 2*nums[j]):
                    count += 1
        return count


# sol -2 using merge sort inversion count but still tle


def merge(nums, l, mid, r):

    i = l
    j = mid

    count = 0

    out = []
    while(i < mid and j <= r):
        if(nums[i] < nums[j]):
            out.append(nums[i])
            i += 1
        else:
            # case of nums[i]>nums[j]

            # since all element to the right of left array is also greater then 2*nums[j]
            # dont forgot this case [-5,-5] to handle this case if left and right el is equal
            # then dont directly inset first into out array bec -5 > -5*2

            k = i
            while(k < mid and nums[k] <= 2*nums[j]):
                k += 1

            if(k <= mid):
                count += (mid-k)

            out.append(nums[j])
            j += 1

    # append remaining elemnt from left sorted array
    while(i < mid):
        out.append(nums[i])
        i += 1
     # append remaining elemnt from right sorted array
    while(j <= r):
        out.append(nums[j])
        j += 1

    # now update orignal array
    for val in out:
        nums[l] = val
        l += 1

    return count


def mergeSort(nums, l, r):
    if(l < r):

        mid = (l+r)/2
        count = 0
        count += mergeSort(nums, l, mid)
        #print "count hai0",count
        count += mergeSort(nums, mid+1, r)
        #print "count hai",count
        #print nums
        count += merge(nums, l, mid+1, r)
        return count

    return 0


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #print nums
        return mergeSort(nums, 0, len(nums)-1)
        #print nums


# slightly optimised version------


def merge(nums, l, mid, r):

    # counti inversions setisfying the conditions
    count = 0

    i = l
    j = mid

    # main modified inversion count logic

    # this j is for 2nd array : just imagine you are moving j variable one at a time
    # and for each j we are moving i (using for left array)  until i<mid and nums[i]<=2*nums[j]
    # and when we get a condition like nums[i]>2*nums[j] then we are increamenting count by
    # (mid-i) why becasue if nums[i] > 2*nums[j] then since left array is sorting it means
    # all elements to the right of ith position will also satsfy nums[i] > 2*nums[j] this condition
    while(j <= r and i < mid):

        while(i < mid and nums[i] <= 2*nums[j]):
            i += 1
        count += (mid-i)

        j += 1

    i = l
    j = mid

    out = []
    while(i < mid and j <= r):
        if(nums[i] < nums[j]):
            out.append(nums[i])
            i += 1
        else:

            out.append(nums[j])
            j += 1

    # append remaining elemnt from left sorted array
    while(i < mid):
        out.append(nums[i])
        i += 1
     # append remaining elemnt from right sorted array
    while(j <= r):
        out.append(nums[j])
        j += 1

    # now update orignal array
    for val in out:
        nums[l] = val
        l += 1

    return count


def mergeSort(nums, l, r):
    if(l < r):

        mid = (l+r)/2
        count = 0
        count += mergeSort(nums, l, mid)
        #print "count hai0",count
        count += mergeSort(nums, mid+1, r)
        #print "count hai",count
        #print nums
        count += merge(nums, l, mid+1, r)
        return count

    return 0


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #print nums
        return mergeSort(nums, 0, len(nums)-1)
        #print nums
