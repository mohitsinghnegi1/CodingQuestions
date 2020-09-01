
# Qus: https: // leetcode.com/problems/merge-intervals/submissions/

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)

        if(n == 0):
            return intervals

        intervals.sort(key=lambda x: (x[0], x[1]))

        out = []
        # initialize a interval
        x, y = intervals[0]

        i = 1
        while(i < n):
            # this is current interval
            x1, y1 = intervals[i]

            # if their is some overlapping than merge these interval
            # dont miss the case [[2 4],[3 3]]
            if(x1 <= y):
                if(y1 > y):
                    y = y1
            # if there is no overlapping with previous interval then append previous             #interval
            else:
                out.append([x, y])
                x, y = x1, y1
            i += 1

        # append the last interval which we had not pushed
        out.append([x, y])
        return out
