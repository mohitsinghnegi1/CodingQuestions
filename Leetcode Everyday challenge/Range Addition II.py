# Qus:https://leetcode.com/problems/range-addition-ii/

# time complexity O(N)
import sys
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_row = m
        min_col = n
        for i in range(len(ops)):
            min_row = min(min_row,ops[i][0])
            min_col = min(min_col,ops[i][1])
        return min_row*min_col
            