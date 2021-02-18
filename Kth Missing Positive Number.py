# Qus:https://leetcode.com/problems/kth-missing-positive-number/

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        j = 1
        for i in range(len(arr)):
            if(arr[i] != j):
                while(arr[i] != j):
                    # you can assume of using a out array where you will push the missing                         # number and append the missing element
                    count += 1
                    # once we reach the pos where missing number reach to k we then return j
                    if(count == k):
                        return j
                    j += 1
            # in case j is equal to cur elemetn it means this elemtn is not missing
            j += 1

        # handle case where k is the missing number bigger then array last element val
        while(True):
            count += 1
            if(count == k):
                return j
            j += 1
