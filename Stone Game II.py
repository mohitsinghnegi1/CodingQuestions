# QUs:https://leetcode.com/problems/stone-game-ii/

"""
    Brute Force : time complexity exponential
"""


import sys


class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        def getMaxScore(piles, m=1, aliceScore=0, aliceTurn=1):

            if(len(piles) == 0):
                return aliceScore

            if(aliceTurn):
                maxSc = 0
                ps = 0
                for i in range(1, min(2*m, len(piles))+1):
                    ps += piles[i-1]
                    sum1 = getMaxScore(piles[i:], max(
                        m, i), aliceScore+ps, aliceTurn ^ 1)
                    if(sum1 > maxSc):
                        maxSc = sum1
                return maxSc

            # elica turn

            minSc = sys.maxsize
            for i in range(1, min(2*m, len(piles))+1):
                sum1 = getMaxScore(piles[i:], max(
                    m, i), aliceScore, aliceTurn ^ 1)
                if(sum1 < minSc):
                    minSc = sum1
            return minSc

        return getMaxScore(piles)
