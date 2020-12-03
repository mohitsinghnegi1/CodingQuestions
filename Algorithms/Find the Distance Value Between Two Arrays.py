# Qus:https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
import bisect

# Optimized Solution
# O(nlogn)


class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """

        count = 0
        # sorting is required to apply binary search
        arr2.sort()

        # traverse in first arr1
        for i in range(len(arr1)):
            # flag will be use to track if there is any element in arr2
            # whose difference is less then d
            flag = True
            # we are tring to obtain a closest value with respect to arr1[i] in arr2
            # as close as possible to reduce the abs distance
            pos = bisect.bisect_left(arr2, arr1[i])

            if(pos == 0 and abs(arr1[i]-arr2[pos]) <= d):
                flag = False
            elif(pos == len(arr2) and abs(arr1[i]-arr2[pos-1]) <= d):
                flag = False

            # we are checking left and right closest value to find min abs distance
            elif(pos != len(arr2) and abs(arr1[i]-arr2[pos]) <= d or abs(arr1[i]-arr2[pos-1]) <= d):

                flag = False

            # if flag is false means there is no value in arr2
            # whose value in not close enough to satisfy the minimum distance
            # condition
            if(flag):

                count += 1

        return count


# brute force solution
# time complexity O(n*2)

class Solution1(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0
        for i in range(len(arr1)):
            flag = True
            for j in range(len(arr2)):
                if(abs(arr1[i]-arr2[j]) <= d):
                    flag = False
                    break
            if(flag):
                count += 1
        return count
