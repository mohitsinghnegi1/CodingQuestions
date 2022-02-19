# Qus:https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)

        d = {}

        def maxScore(cardPoints, k, i, j):

            if(k == 0):
                return 0
            if((i, j) in d):
                return d[(i, j)]

            left = cardPoints[i] + maxScore(cardPoints, k-1, i+1, j)
            right = cardPoints[j] + maxScore(cardPoints, k-1, i, j-1)

            d[(i, j)] = max(left, right)
            return d[(i, j)]

        return maxScore(cardPoints, k, 0, n-1)


# solution 2

"""
Minimise the middle subarray of len n-k to max the outer part (Sliding window)
"""


class Solution2(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)

        sum1 = 0
        i = 0
        while(i < n-k):
            sum1 += cardPoints[i]
            i += 1

        total = sum(cardPoints)
        print sum1
        # now we have one range sum , we need to minimise it to maximise the  ans
        min1 = sum1
        j = 0
        while(i < n):
            sum1 += (cardPoints[i]-cardPoints[j])
            # print sum1
            min1 = min(min1, sum1)
            j += 1
            i += 1

        return total-min1
