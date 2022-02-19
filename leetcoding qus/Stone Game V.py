# Qus:https://leetcode.com/problems/stone-game-v/

# even after using memorization still giving tle
class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """

        n = len(stoneValue)

        d = [[-1]*n for i in range(n)]

        def getAliceScore(l, r):

            if(l >= r):
                return 0
            if(d[l][r] != -1):
                return d[l][r]

            rightSum = 0
            for i in range(l, r+1):
                rightSum += stoneValue[i]
            # print rightSum
            leftSum = 0
            ans = 0
            for i in range(l, r+1):
                leftSum += stoneValue[i]
                rightSum -= stoneValue[i]

                if(leftSum < rightSum):
                    ans = max(ans, leftSum+getAliceScore(l, i))
                if(leftSum == rightSum):
                    ans = max(ans, leftSum +
                              max(getAliceScore(l, i), getAliceScore(i+1, r)))
                if(leftSum > rightSum):
                    ans = max(ans, rightSum+getAliceScore(i+1, r))

            d[l][r] = ans
            return d[l][r]

#
