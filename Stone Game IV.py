# QUs:https://leetcode.com/problems/stone-game-iv/

import math


class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = {}

        def canAliceWin(n, turn=1):

            if((n, turn) in d):
                return d[(n, turn)]
            if(n == 0):
                # turn of bob return true else return false
                return not turn
            if(turn):

                d[(n, turn)] = any(canAliceWin(n-i**2, turn ^ 1)
                                   for i in range(1, int(math.sqrt(n)+1)))
                return d[(n, turn)]
            else:
                # any case where alica is not wining

                for i in range(1, int(math.sqrt(n)+1)):

                    if(not canAliceWin(n-i**2, turn ^ 1)):
                        d[(n, turn)] = False
                        return d[(n, turn)]
                d[(n, turn)] = True
                return d[(n, turn)]

        ans = canAliceWin(n)
        # print d
        return ans
