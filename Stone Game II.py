# QUs:https://leetcode.com/problems/stone-game-ii/

"""
    Brute Force : time complexity exponential
    Alica will try to maximize his score
    and bob will try to minimize alice score
    at the end the max score that alica can make we need to return it
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


"""
    TIme complexity n**2
    relative score we need to find then apply formula 

"""


class Solution2(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)

        total = sum(piles)

        # n + 1 just to remove a corner case where m =1
        d = [[-1]*(n+1) for i in range(n+1)]

        # x denotes the stating point for the player
        def getRelativeScore(x, m):
            # if the given begin index greater of eql to len then return 0 as score
            if(x >= len(piles)):
                return 0

            if(d[x][m] != -1):
                return d[x][m]

            maxSc = -sys.maxsize  # since we want max value of stone that alica can get
            tot = 0  # tot will keep on incrementing until 2*m

            # at max we can pick 2 m piles
            for i in range(0, 2*m):
                # let say i pic only 1
                # at max we can go to len(piles)
                if(x+i < len(piles)):
                    # let say we pick piles from x to i
                    tot += piles[x+i]

                    # my relative score will be the the pile that i have picked -
                    # the relative score of other player
                    sc = (tot - getRelativeScore(x+i+1, max(m, i+1)))

                    maxSc = max(maxSc, sc)

            # we have the max relative score of alice at the end
            # which will give max score of alice
            d[x][m] = maxSc
            return d[x][m]

        relativeSc = getRelativeScore(0, 1)
        # print relativeSc

        # relativeSc =  a - b
        # total = a + b
        # b= a - relative
        # total = a + a - relative
        # (total + relative) /2
        return (total+relativeSc)/2
