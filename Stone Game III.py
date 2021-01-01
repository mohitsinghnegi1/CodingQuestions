# QUs: https: // leetcode.com/problems/stone-game-iii/

# Brute Force: Time complexity O(3**n)

import sys


class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        total = sum(stoneValue)

        def relativeScoreOfAlice(stoneValue, score=0):

            if(len(stoneValue) == 0):
                return 0

            maxSc = -sys.maxsize
            sum1 = 0
            for i in range(min(3, len(stoneValue))):
                sum1 += stoneValue[i]
                sc = sum1-relativeScoreOfAlice(stoneValue[i+1:])
                maxSc = max(sc, maxSc)

            return maxSc

        relativeScore = relativeScoreOfAlice(stoneValue)

        if(relativeScore == 0):
            return "Tie"
        if(relativeScore > 0):
            return "Alice"
        return "Bob"


# Optimized solution using bottom up apporach (recursion) with memorization


class Solution2(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        total = sum(stoneValue)

        d = {}

        def relativeScoreOfAlice(stoneValue, idx=0):
            if(idx in d):
                return d[idx]

            if(idx == len(stoneValue)):
                return 0

            maxSc = -sys.maxsize
            sum1 = 0
            for i in range(idx, min(idx+3, len(stoneValue))):
                sum1 += stoneValue[i]
                sc = sum1-relativeScoreOfAlice(stoneValue, i+1)
                maxSc = max(sc, maxSc)

            d[idx] = maxSc
            return d[idx]

        relativeScore = relativeScoreOfAlice(stoneValue)

        if(relativeScore == 0):
            return "Tie"
        if(relativeScore > 0):
            return "Alice"
        return "Bob"
