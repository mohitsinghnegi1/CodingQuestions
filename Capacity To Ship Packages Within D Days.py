# Qus:https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """

        l = max(weights)
        r = sum(weights)+1

        while(l < r):

            mid = l + (r - l)/2

            cur = 0
            part = 1
            for val in weights:
                if(cur + val > mid):
                    part += 1
                    cur = val

                else:
                    cur += val

            if part <= D:
                # we can utilize mnore part to dec average
                r = mid
            else:
                l = mid+1

        return l
