# Qus:https://leetcode.com/problems/pancake-sorting/

def reverse(arr, l, r):

    while(l < r):
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1


class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)

        # this sortarr will keep track of max index
        sortedarr = sorted(arr, reverse=True)

        # sort[k] will be the val of next greater eleemnt,last will be the last index we need           # to put max value eleement
        k, last = 0, n-1
        out = []
        for i in range(n):
            # find max element index
            # we arr using arr.index instead of maintaining arr index before hand bec
            # the index is changing again an again
            maxIndex = arr.index(sortedarr[k], 0, n-i)
            # it will contibute to ans
            out.append(maxIndex+1)
            # reverse up to that index
            reverse(arr, 0, maxIndex)
            # print arr,maxIndex
            # last index will be pushed as we will reverse arr up to that index
            out.append(last+1)
            # reverse again with the updated last pos
            reverse(arr, 0, last)
            # increement k so that we can get next greater element index
            k += 1
            # decrement the last where we need to keep next largest element
            last -= 1
            # print arr

        return out
