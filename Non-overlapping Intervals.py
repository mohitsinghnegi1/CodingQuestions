# Qus:https://leetcode.com/problems/non-overlapping-intervals/

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[1]))

        x1, y1 = intervals[0]
        count = 0
        i = 1
        while(i < len(intervals)):
            x2, y2 = intervals[i]

            if(x2 < y1):
                count += 1  # remove this
            else:
                x1, y1 = x2, y2
            i += 1
        return count
