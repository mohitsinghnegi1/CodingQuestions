# Qus:https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        res = 0

        while(len(arr) > 1):
            # pick the smallest element index
            idx = arr.index(min(arr))

            # pick the smallest of left and right element of smallest element
            # why bec , we want to minimize the overall sum which is possible only when
            # we pick the min elemt and pick 2nd element which will produce min result
            # product of both element will be contibute to res as it will be a non leaf node
            if(idx == 0):
                res += arr[idx]*arr[idx+1]
            elif(idx == len(arr)-1):
                res += arr[idx]*arr[idx-1]
            else:
                res += arr[idx]*min(arr[idx-1], arr[idx+1])
            # pop out the minimum element as it will not contibute to ans again
            arr.pop(idx)
        # return non leaf res sum
        return res
