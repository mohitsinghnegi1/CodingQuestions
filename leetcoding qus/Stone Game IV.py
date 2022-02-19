# QUs:https://leetcode.com/problems/stone-game-iv/

import math


class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = [[-1]*2 for i in range(n+1)]

        def canAliceWin(n, turn=1):

            if(d[n][turn] != -1):
                return d[n][turn]
            if(n == 0):
                # turn of bob return true else return false
                return not turn
            if(turn):
                # if its bob turn then choose any sq by choosing which alice can win (dont use any()
                #  # takes more time)
                for i in range(1, int(math.sqrt(n)+1)):
                    if(canAliceWin(n-i**2, turn ^ 1)):
                        d[n][turn] = True
                        return d[n][turn]

                d[n][turn] = False
                return d[n][turn]

            # any case where alica is not wining

            for i in range(1, int(math.sqrt(n)+1)):
                # choose any sq by using which alica can not win
                if(not canAliceWin(n-i**2, turn ^ 1)):
                    d[n][turn] = False
                    return d[n][turn]

            d[n][turn] = True
            return d[n][turn]

        ans = canAliceWin(n)
        # print d
        return ans


# more optimised solution (Instead of starting from 1 to sqrt(n) we can find solution in  reverse order to reach to solution fast)
# here we are using top down approach
class Solution2(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = [[-1]*2 for i in range(n+1)]

        def canAliceWin(n, turn=1):

            if(d[n][turn] != -1):
                return d[n][turn]
            if(n == 0):
                # turn of bob return true else return false
                return not turn
            if(turn):
                # if its bob turn then choose any sq by choosing which alice can win (dont use any()
                # # takes more time)
                for i in range(int(math.sqrt(n)), 0, -1):
                    if(canAliceWin(n-i**2, turn ^ 1)):
                        d[n][turn] = True
                        return d[n][turn]

                d[n][turn] = False
                return d[n][turn]

            # any case where alica is not wining

            for i in range(int(math.sqrt(n)), 0, -1):
                # choose any sq by using which alica can not win
                if(not canAliceWin(n-i**2, turn ^ 1)):
                    d[n][turn] = False
                    return d[n][turn]

            d[n][turn] = True
            return d[n][turn]

        ans = canAliceWin(n)
        # print d
        return ans
